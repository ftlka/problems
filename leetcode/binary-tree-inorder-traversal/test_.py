from solution import TreeNode, Solution


s = Solution()

# test 1
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

assert s.inorderTraversal(root) == [1, 3, 2]


# test 2
root = TreeNode(1)
left = TreeNode(2)
left.left, left.right = TreeNode(3), TreeNode(4)
right = TreeNode(5)
right.left, right.right = TreeNode(6), TreeNode(7)
root.left, root.right = left, right

assert s.inorderTraversal(root) == [3, 2, 4, 1, 6, 5, 7]


# test 3
root = TreeNode(2)
left = TreeNode(3)
left.left = TreeNode(1)
root.left = left

assert s.inorderTraversal(root) == [1, 3, 2]
