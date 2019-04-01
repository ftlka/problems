class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
    	cur_node = root
    	while True:
    		# if they're on different sides
    		if (p.val < cur_node.val and q.val > cur_node.val) or (p.val > cur_node.val and q.val < cur_node.val):
    			return cur_node
    		if p == cur_node or q == cur_node:
    			return cur_node
    		# we descend deeper
    		if q.val < cur_node.val:
    			cur_node = cur_node.left
    		else:
    			cur_node = cur_node.right
        