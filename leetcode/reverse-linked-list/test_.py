from solution import ListNode, Solution


s = Solution()

node = head = ListNode(0)
for el in range(1, 6):
	node.next = ListNode(el)
	node = node.next

reversed_l = s.reverseList(head)
for i in range(5, -1, -1):
	assert reversed_l.val == i
	reversed_l = reversed_l.next

assert s.reverseList(ListNode(0)).val == 0
