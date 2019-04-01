from solution import TreeNode, Solution


s = Solution()

# first test
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)

assert s.tree2str(root) == '1(2(4))(3)'


# second test
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(4)

assert s.tree2str(root) == '1(2()(4))(3)'


# third test
assert s.tree2str(None) == ''


# fourth test
root = TreeNode(1)
root.right = TreeNode(3)

assert s.tree2str(root) == '1()(3)'
