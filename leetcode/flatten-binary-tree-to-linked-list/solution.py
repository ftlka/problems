from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def flatten(self, root):
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
        	return

        stack = deque()
        current_node = root
        last_added_node = None

        while True:
        	if current_node.right:
	        	stack.append(current_node.right)

        	if current_node.left:
	        	stack.append(current_node.left)

	        if not stack:
        		break

        	current_node.left, current_node.right = None, stack.pop()
        	current_node = current_node.right
        	last_added_node = current_node


        if last_added_node:
        	last_added_node.next = None

        