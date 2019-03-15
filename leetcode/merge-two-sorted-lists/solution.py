class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1, l2):
        res = root = ListNode(0)
        while l1 or l2:
            if l1 and l2:
                if l1.val < l2.val:
                    root.next = l1
                    l1 = l1.next
                    root = root.next
                else:
                    root.next = l2
                    l2 = l2.next
                    root = root.next
            else:
                if l1:
                    root.next = l1
                    l1 = l1.next
                    root = root.next
                else:
                    root.next = l2
                    l2 = l2.next
                    root = root.next

        return res.next
        