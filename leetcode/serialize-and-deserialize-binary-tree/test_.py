from solution import TreeNode, Codec


def traverse(node, nodes):
	nodes.append(node.val if node else None)


	if node:
		traverse(node.left, nodes)
		traverse(node.right, nodes)


codec = Codec()


# test 1
root = TreeNode(1)
root.left = TreeNode(2)
right = TreeNode(3)
right.left, right.right = TreeNode(4), TreeNode(5)
root.right = right

deserialized = codec.deserialize(codec.serialize(root))

original_nodes = []
deser_nodes = []
traverse(root, original_nodes)
traverse(deserialized, deser_nodes)

assert original_nodes == deser_nodes


# test 2
root = TreeNode(1)
right = TreeNode(2)
right.right = TreeNode(3)
root.right = right

deserialized = codec.deserialize(codec.serialize(root))

original_nodes = []
deser_nodes = []
traverse(root, original_nodes)
traverse(deserialized, deser_nodes)

assert original_nodes == deser_nodes


# test 3
root = TreeNode(1)
root.left = TreeNode(2)

deserialized = codec.deserialize(codec.serialize(root))

original_nodes = []
deser_nodes = []
traverse(root, original_nodes)
traverse(deserialized, deser_nodes)

assert original_nodes == deser_nodes


# test 4
root = TreeNode(1)
root.right = TreeNode(2)

deserialized = codec.deserialize(codec.serialize(root))

original_nodes = []
deser_nodes = []
traverse(root, original_nodes)
traverse(deserialized, deser_nodes)

assert original_nodes == deser_nodes


# test 5
root = TreeNode(1)
left = TreeNode(2)
left.left, left.right = TreeNode(3), TreeNode(4)
root.left, root.right = left, TreeNode(5)

deserialized = codec.deserialize(codec.serialize(root))

original_nodes = []
deser_nodes = []
traverse(root, original_nodes)
traverse(deserialized, deser_nodes)

assert original_nodes == deser_nodes


# test 6
root = TreeNode(3)
left = TreeNode(2)
left.left = TreeNode(1)
root.left, root.right = left, TreeNode(4)

deserialized = codec.deserialize(codec.serialize(root))

original_nodes = []
deser_nodes = []
traverse(root, original_nodes)
traverse(deserialized, deser_nodes)

assert original_nodes == deser_nodes
