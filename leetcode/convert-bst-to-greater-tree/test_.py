from solution import TreeNode, Solution


def traverse(node, nodes):
	nodes.append(node.val)
	if node.left:
		traverse(node.left, nodes)
	if node.right:
		traverse(node.right, nodes)
	return nodes


s = Solution()

# test 1
root = TreeNode(5)
root.left = TreeNode(2)
root.right = TreeNode(13)

res = s.convertBST(root)

assert traverse(res, []) == [18, 20, 13]


# test 2
assert s.convertBST(None) is None


# test 3
root = TreeNode(2)
left = TreeNode(0)
left.left, left.right = TreeNode(-4), TreeNode(1)
root.left, root.right = left, TreeNode(3)

res = s.convertBST(root)

assert traverse(res, []) == [5, 6, 2, 6, 3]


# test 4
root = TreeNode(1)
left, right = TreeNode(0), TreeNode(4)
left.left, right.left = TreeNode(-2), TreeNode(3)
root.left, root.right = left, right

res = s.convertBST(root)

assert traverse(res, []) == [8, 8, 6, 4, 7]
