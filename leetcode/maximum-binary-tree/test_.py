from solution import TreeNode, Solution


def traverse(node, ar):
	ar.append(node.val)
	if node.left:
		traverse(node.left, ar)
	if node.right:
		traverse(node.right, ar)
	return ar


s = Solution()

root = TreeNode(6)
left, right = TreeNode(3), TreeNode(5)
left.right, right.left = TreeNode(2), TreeNode(0)
left.right.right = TreeNode(1)
root.left, root.right = left, right

assert traverse(s.constructMaximumBinaryTree([3, 2, 1, 6, 0, 5]), []) == traverse(root, [])
