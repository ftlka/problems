class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution(object):
    def levelOrder(self, root):
        if not root:
            return []
        res = [[root.val]]
        cur_level = root.children
        next_level = []

        while cur_level:
            cur_ar = []
            for node in cur_level:
                cur_ar.append(node.val)
                next_level.extend(node.children)
            res.append(cur_ar)
            cur_level = next_level
            next_level = []

        return res
        