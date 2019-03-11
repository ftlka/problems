from solution import Solution


def traverse_inorder(node, res):
	if node.left:
		traverse_inorder(node.left, res)
	res.append(node.val)	
	if node.right:
		traverse_inorder(node.right, res)

	return res


s = Solution()
# basic tests
preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]
root = s.buildTree(preorder, inorder)
assert traverse_inorder(root, []) == inorder

preorder = [1, 2, 3]
inorder = [2, 3, 1]
root = s.buildTree(preorder, inorder)
assert traverse_inorder(root, []) == inorder

# empty tree
assert s.buildTree([], []) == None

preorder = [3, 9, 4, 5, 20, 15, 7]
inorder = [4, 9, 5, 3, 15, 20, 7]
root = s.buildTree(preorder, inorder)
assert traverse_inorder(root, []) == inorder