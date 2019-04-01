from solution import Node, Solution


def traverse(node, ar):
	ar.append(node.val)
	for child_node in node.children:
		traverse(child_node, ar)
	return ar


s = Solution()

left = Node(val=3, children=[Node(val=5, children=[]), Node(val=6, children=[])])
center = Node(val=2, children=[])
right = Node(val=4, children=[])
root = Node(val=1, children=[left, center, right])

assert s.preorder(root) == traverse(root, [])

assert s.preorder(None) == []
