from solution import TreeNode, Solution


s = Solution()


root = TreeNode(4)
left, right = TreeNode(2), TreeNode(7)
left.left, left.right = TreeNode(1), TreeNode(3)
right.left, right.right = TreeNode(6), TreeNode(9)
root.left, root.right = left, right

inverted_root = s.invertTree(root)

# im too lazy
assert inverted_root.val == 4
assert (inverted_root.left.val, inverted_root.right.val) == (7, 2)
assert (inverted_root.left.left.val, inverted_root.left.right.val) == (9, 6)
assert (inverted_root.right.left.val, inverted_root.right.right.val) == (3, 1)
