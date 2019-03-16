class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rec(self, node):
        if not node:
            return
        node.left, node.right = node.right, node.left
        self.rec(node.left)
        self.rec(node.right)

    def invertTree(self, root):
        self.rec(root)
        return root
        