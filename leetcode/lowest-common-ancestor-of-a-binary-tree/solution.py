class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def find_lca(self, node, p, q):
        if node == p or node == q:
            return node

        if not (node.left or node.right):
            return None

        left = None
        if node.left:
            left = self.find_lca(node.left, p, q)
        right = None
        if node.right:
            right = self.find_lca(node.right, p, q)

        if right and left:
            return node
        else:
            return left if left else right

    def lowestCommonAncestor(self, root, p, q):
        return self.find_lca(root, p, q)
        