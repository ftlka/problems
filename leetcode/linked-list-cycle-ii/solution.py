class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def detectCycle(self, head):
    	if not head or not head.next:
    		return None

    	slow, fast = head.next, head.next.next
    	while slow != fast:
    		if not fast or not fast.next:
    			return None
    		slow = slow.next
    		fast = fast.next.next

    	if slow != fast:
    		return None

    	new_head = head
    	while new_head != slow:
    		new_head = new_head.next
    		slow = slow.next
    	return slow
        