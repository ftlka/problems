class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def rec(self, cur_bst, acc_sum):
        if cur_bst.right:
            right, acc_sum = self.rec(cur_bst.right, acc_sum)
            current_g = TreeNode(cur_bst.val + acc_sum)
            current_g.right = right
        else:
            current_g = TreeNode(cur_bst.val + acc_sum)
        acc_sum = cur_bst.val + acc_sum


        if cur_bst.left:
            left, acc_sum = self.rec(cur_bst.left, acc_sum)
            current_g.left = left

        return current_g, acc_sum


    def convertBST(self, root):
        if not root:
            return

        return self.rec(root, 0)[0]
        