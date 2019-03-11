class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def _buildTree(self, preorder, inorder, node, self_idx_pre, self_idx_in, left_bound, right_bound):
        if self_idx_pre == len(preorder) - 1:
            return
        # how many do we skip to get to the right child
        nodes_to_the_left = 0

        # we want to check if next node is left
        if self_idx_in > left_bound:
            # there's something to the left
            left_pre_idx = self_idx_pre + 1
            node.left = TreeNode(preorder[left_pre_idx])
            left_in_idx = inorder.index(node.left.val)
            nodes_to_the_left += self_idx_in - left_bound
            self._buildTree(preorder, inorder, node.left, left_pre_idx, left_in_idx, left_bound, self_idx_in - 1)

        if self_idx_in < right_bound:
            # there's something to the right
            right_pre_idx = self_idx_pre + nodes_to_the_left + 1
            node.right = TreeNode(preorder[right_pre_idx])
            right_in_idx = inorder.index(node.right.val)
            self._buildTree(preorder, inorder, node.right, right_pre_idx, right_in_idx, self_idx_in + 1, right_bound)

    def buildTree(self, preorder, inorder):
        if not preorder:
            return

        root = TreeNode(preorder[0])
        # bounds not including, so they are -1 for left and +1 for right
        self._buildTree(preorder, inorder, root, 0, inorder.index(root.val), 0, len(preorder) - 1)
        return root
        