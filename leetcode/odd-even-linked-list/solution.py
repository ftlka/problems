class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def oddEvenList(self, head):
        even_head = ListNode(0)
        odd = ListNode(0)
        root = odd
        counter = 1

        while head:
            if counter % 2 == 0:
                # if its a first node we attach
                if not even_head.next:
                    cur_even = ListNode(head.val)
                    even_head.next = cur_even
                else:
                    cur_even.next = ListNode(head.val)
                    cur_even = cur_even.next
            else:
                odd.next = ListNode(head.val)
                odd = odd.next

            head = head.next
            counter += 1

        # attaching even head to odd tail
        odd.next = even_head.next
        return root.next
