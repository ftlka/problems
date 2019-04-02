from solution import TreeNode, Solution


s = Solution()

# first test
root = TreeNode(1)
left, right = TreeNode(1), TreeNode(1)
left.left, left.right = TreeNode(1), TreeNode(1)
right.right = TreeNode(1)
root.left, root.right = left, right

assert s.isUnivalTree(root)


# second test
assert s.isUnivalTree(None)


# third test
root = TreeNode(2)
left, right = TreeNode(2), TreeNode(2)
left.left, left.right = TreeNode(5), TreeNode(2)
root.left, root.right = left, right

assert not s.isUnivalTree(root)
