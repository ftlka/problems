from collections import deque


class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution(object):
    def preorder(self, root):
        if not root:
            return []

        res = []
        queue = deque()
        queue.append(root)
        
        while queue:
            cur_node = queue.pop()
            res.append(cur_node.val)
            for child_node in reversed(cur_node.children):
                queue.append(child_node)

        return res
        