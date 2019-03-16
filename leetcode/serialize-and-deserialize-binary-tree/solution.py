from collections import deque


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def rec(self, node, nodes):
        if node:
            nodes.append(str(node.val))
            self.rec(node.left, nodes)
            self.rec(node.right, nodes)
        else:
            nodes.append('None')

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        nodes = []
        self.rec(root, nodes)
        return ','.join(nodes)      

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = data.split(',')
        stack = deque()

        if data[0] == 'None':
            return
        else:
            current_node = root = TreeNode(int(data[0]))

        stack.append(current_node)
        i = 1
        while i < len(data):
            if data[i] != 'None':
                # if we need to add left
                if not stack[-1].left and data[i-1] != 'None':
                    cur_node = TreeNode(int(data[i]))
                    stack[-1].left = cur_node
                    stack.append(cur_node)
                else:
                    cur_node = TreeNode(int(data[i]))
                    stack[-1].right = cur_node
                    stack.pop()
                    stack.append(cur_node)
            # two Nones in a row
            elif i + 1 >= len(data) or data[i+1] == 'None':
                if stack:
                    stack.pop()
            i += 1

        return root

