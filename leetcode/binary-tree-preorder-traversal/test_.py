from solution import TreeNode, Solution


def rec_preorder(node, ar):
	ar.append(node.val)
	if node.left:
		rec_preorder(node.left, ar)
	if node.right:
		rec_preorder(node.right, ar)


s = Solution()


# test 1
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

nodes = []
rec_preorder(root, nodes)
assert s.preorderTraversal(root) == nodes


# test 2
root = TreeNode(1)
left, right = TreeNode(2), TreeNode(3)
left.left, left.right = TreeNode(4), TreeNode(5)
right.left, right.right = TreeNode(6), TreeNode(7)
root.left, root.right = left, right

nodes = []
rec_preorder(root, nodes)
assert s.preorderTraversal(root) == nodes


# test 3
assert s.preorderTraversal(None) == []
