class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head):
        prev = head
        if head and head.next:
            head = head.next
        else:
            return head
        prev.next = None

        while head and head.next:
            over_one = head.next
            head.next = prev
            prev = head
            head = over_one
        head.next = prev

        return head
        