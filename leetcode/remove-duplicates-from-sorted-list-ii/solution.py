class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return

        new_head = ListNode(-1)
        new_head.next = head
        prev = new_head
        cur = new_head.next

        while cur and cur.next:
            if cur.next.val != cur.val:
                prev = cur
                cur = cur.next
            else:
                while cur.next and cur.val == cur.next.val:
                    cur = cur.next
                cur = cur.next
                prev.next = cur

        return new_head.next
        