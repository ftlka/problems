class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def rec(self, node):
        s = ''
        if not node:
            return s
        s += str(node.val)
        if node.left or node.right:
            s += '('
            if node.left:
                s += self.rec(node.left)
            s += ')'
            if node.right:
                s += '(' + self.rec(node.right) + ')'
        return s


    def tree2str(self, t):
        return self.rec(t)
        