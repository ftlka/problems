class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def rec(self, parent, node):
        if node.left:
            self.rec(node, node.left)
        if node.right:
            self.rec(node, node.right)
        if not (node.left or node.right) and node.val == 0:
            if parent.left == node:
                parent.left = None
            else:
                parent.right = None

    def pruneTree(self, root):
        if not root:
            return None

        if root.left:
            self.rec(root, root.left)
        if root.right:
            self.rec(root, root.right)


        return root
        