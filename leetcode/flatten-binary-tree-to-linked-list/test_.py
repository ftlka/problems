from solution import TreeNode, Solution

s = Solution()

root = TreeNode(1)
left, right = TreeNode(2), TreeNode(5)
left.left, left.right, right.right = TreeNode(3), TreeNode(4), TreeNode(6)
root.left, root.right = left, right

s.flatten(root)

ar = [1, 2, 3, 4, 5, 6]
for el in ar:
	assert root.val == el

	if root and root.right:
		root = root.right
