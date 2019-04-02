class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def find_max(self, ar, start_i, end_i):
        max_i = start_i
        while start_i <= end_i:
            if ar[start_i] > ar[max_i]:
                max_i = start_i
            start_i += 1

        return max_i

    def create_node(self, node, i, start_i, end_i, ar):
        if i - start_i > 0:
            left_max_i = self.find_max(ar, start_i, i - 1)
            left = TreeNode(ar[left_max_i])
            self.create_node(left, left_max_i, start_i, i - 1, ar)
            node.left = left
        if end_i - i > 0:
            right_max_i = self.find_max(ar, i + 1, end_i)
            right = TreeNode(ar[right_max_i])
            self.create_node(right, right_max_i, i + 1, end_i, ar)
            node.right = right

    def constructMaximumBinaryTree(self, nums):
        if not nums:
            return None

        root_idx = self.find_max(nums, 0, len(nums) - 1)
        root = TreeNode(nums[root_idx])
        self.create_node(root, root_idx, 0, len(nums) - 1, nums)

        return root        
        