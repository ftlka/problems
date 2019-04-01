from solution import Node, Solution


s = Solution()

left = Node(val=3, children=[Node(val=5, children=[]), Node(val=6, children=[])])
center = Node(val=2, children=[])
right = Node(val=4, children=[])
root = Node(val=1, children=[left, center, right])


assert s.levelOrder(root) == [[1], [3, 2, 4], [5, 6]]

assert s.levelOrder(None) == []
