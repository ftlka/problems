from solution import Solution, TreeNode

s = Solution()

# basic tests
# [3, 9, 20, null, null, 15, 7]
root = TreeNode(3)
root.left = TreeNode(9)
right = TreeNode(20)
right.left, right.right = TreeNode(15), TreeNode(7)
root.right = right

answer = [
	[3],
	[20, 9],
	[15, 7]
]
actual = s.zigzagLevelOrder(root)
assert actual == answer

# empty tree
assert s.zigzagLevelOrder(None) == []

# empty in between
# [1, 2, 3, 4, null, null, 5]
root = TreeNode(1)
left = TreeNode(2)
right = TreeNode(3)
left.left, right.right = TreeNode(4), TreeNode(5)
root.left, root.right = left, right

answer = [
	[1],
	[3, 2],
	[4, 5]
]
assert s.zigzagLevelOrder(root) == answer