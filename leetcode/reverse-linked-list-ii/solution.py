class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseBetween(self, head, m, n):
        orig_head = ListNode(-1)
        orig_head.next = head
        cur_node = orig_head.next
        if m == n:
            return orig_head.next

        i = 1
        while i < m - 1:
            cur_node = cur_node.next
            i += 1
        start = cur_node
        if m == 1:
            first_node = prev = cur_node
        else:
            first_node = prev = cur_node.next            

        if not cur_node.next:
            return orig_head.next
        cur_node = prev.next

        i = m + 1
        while i < n:
            next_node = cur_node.next
            cur_node.next = prev
            prev = cur_node
            cur_node = next_node
            i += 1

        first_node.next = cur_node.next
        if m != 1:
            start.next = cur_node
        else:
            orig_head.next = cur_node

        cur_node.next = prev

        return orig_head.next
        