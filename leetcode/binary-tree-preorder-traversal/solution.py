from collections import deque


class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


class Solution(object):
	def preorderTraversal(self, root):
		if not root:
			return []
		nodes = []
		q = deque()
		q.append(root)

		while q:
			cur_node = q.pop()
			nodes.append(cur_node.val)
			if cur_node.right:
				q.append(cur_node.right)
			if cur_node.left:
				q.append(cur_node.left)

		return nodes
	