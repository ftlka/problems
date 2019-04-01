from solution import TreeNode, Solution


def traverse(node, ar):
	ar.append(node.val)
	if node.left:
		traverse(node.left, ar)
	else:
		ar.append(None)
	if node.right:
		traverse(node.right, ar)
	else:
		ar.append(None)
	return ar


s = Solution()

# first test
root = TreeNode(1)
right = TreeNode(0)
right.left, right.right = TreeNode(0), TreeNode(1)
root.right = right

answ_root = TreeNode(1)
answ_root.right, answ_root.right.right = TreeNode(0), TreeNode(1)


assert traverse(s.pruneTree(root), []) == traverse(answ_root, [])


# second test
root = TreeNode(1)
left, right = TreeNode(0), TreeNode(1)
left.left, left.right = TreeNode(0), TreeNode(0)
right.left, right.right = TreeNode(0), TreeNode(1)
root.left, root.right = left, right

answ_root = TreeNode(1)
answ_root.right, answ_root.right.right = TreeNode(1), TreeNode(1)

assert traverse(s.pruneTree(root), []) == traverse(answ_root, [])


# third test
root = TreeNode(1)
left, right = TreeNode(1), TreeNode(0)
left.left, left.right = TreeNode(1), TreeNode(1)
left.left.left = TreeNode(0)
right.left, right.right = TreeNode(0), TreeNode(1)
root.left, root.right = left, right

answ_root = TreeNode(1)
left, right = TreeNode(1), TreeNode(0)
left.left, left.right = TreeNode(1), TreeNode(1)
right.right = TreeNode(1)
answ_root.left, answ_root.right = left, right

assert traverse(s.pruneTree(root), []) == traverse(answ_root, [])
