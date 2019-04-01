from solution import TreeNode, Solution


s = Solution()


root = TreeNode(6)
root.left = TreeNode(2)
root.right = TreeNode(8)
root.left.right = TreeNode(4)

assert s.lowestCommonAncestor(root, root.left, root.right) == root

assert s.lowestCommonAncestor(root, root.left, root.left.right) == root.left

assert s.lowestCommonAncestor(root, root.right, root) == root
