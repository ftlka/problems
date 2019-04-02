from solution import TreeNode, Solution


s = Solution()

# first test
root = TreeNode(3)
left, right = TreeNode(5), TreeNode(1)
left.left, left.right = TreeNode(6), TreeNode(2)
left.right.left, left.right.right = TreeNode(7), TreeNode(4)
right.left, right.right = TreeNode(0), TreeNode(8)
root.left, root.right = left, right

assert s.lowestCommonAncestor(root, root.left, root.right) == root

assert s.lowestCommonAncestor(root, root.right, root.left) == root

assert s.lowestCommonAncestor(root, root.left, root) == root

assert s.lowestCommonAncestor(root, root, root.right) == root

assert s.lowestCommonAncestor(root, root.left, root.left.right.right) == root.left

assert s.lowestCommonAncestor(root, root.left.right.left, root.left.left) == root.left


# second test
root = TreeNode(1)
left, right = TreeNode(2), TreeNode(3)
left.right = TreeNode(4)
root.left, root.right = left, right

assert s.lowestCommonAncestor(root, root.left.right, root.right) == root
