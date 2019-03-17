from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root):
        if not root:
            return []

        res = []
        stack = deque()
        stack.append(root)
        cur_node = root

        while True:
            while cur_node and cur_node.left:
                cur_node = cur_node.left
                stack.append(cur_node)

            if not stack:
                return res

            cur_node = stack.pop()
            res.append(cur_node.val)
            cur_node = cur_node.right
            if cur_node:
                stack.append(cur_node)
            
