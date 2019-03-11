class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head):
        # find the middle node
        slow = fast = head
        i = 0
        while fast and fast.next:
            i += 1
            slow = slow.next
            fast = fast.next.next
        
        # now we reverse it
        prev = None
        while slow:
            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node
        slow = prev

        # and now compare
        while slow and head:
            if slow.val != head.val:
                return False
            slow = slow.next
            head = head.next

        return True
        