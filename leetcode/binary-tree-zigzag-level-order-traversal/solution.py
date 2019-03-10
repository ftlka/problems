from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def traverse(self, node, res, cur_level_res, cur_level, next_level):
        cur_level_res.append(node.val)
        if node.left or node.right:
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)

        if cur_level:
            self.traverse(cur_level.popleft(), res, cur_level_res, cur_level, next_level)
        else:
            if len(res) % 2 == 1:
                cur_level_res.reverse()
            res.append(cur_level_res)

            if next_level:
                self.traverse(next_level.popleft(), res, [], next_level, deque())

    def zigzagLevelOrder(self, root):
        if not root:
            return []

        res = []
        cur_level_res = []
        cur_level = deque()
        next_level = deque()
        self.traverse(root, res, cur_level_res, cur_level, next_level)

        return res
        