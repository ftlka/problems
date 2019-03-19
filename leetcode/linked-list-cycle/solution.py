class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head):
    	if not head:
    		return False

    	slow, fast = head, head.next

    	while fast and fast.next:
    		if fast == slow:
    			return True
    		fast, slow = fast.next.next, slow.next

    	return False
        