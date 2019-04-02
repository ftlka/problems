from collections import deque


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isUnivalTree(self, root):
        if not root:
            return True

        val = root.val
        queue = deque()
        queue.appendleft(root)

        while queue:
            cur_node = queue.pop()

            if cur_node.val != val:
                return False

            if cur_node.left:
                queue.appendleft(cur_node.left)
            if cur_node.right:
                queue.appendleft(cur_node.right)
        
        return True        
        