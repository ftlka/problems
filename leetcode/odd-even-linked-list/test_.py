from solution import ListNode, Solution

sol = Solution()

# first test
# 1->2->3->4->5->NULL
head = ListNode(1)
cur = head
for i in range(2, 6):
	cur.next = ListNode(i)
	cur = cur.next

new_head = sol.oddEvenList(head)
vals = [1, 3, 5, 2, 4]
for val in vals:
	assert val == new_head.val
	new_head = new_head.next


# second test
# 2->1->3->5->6->4->7->NULL
head = ListNode(2)
cur = head
nodes = [1, 3, 5, 6, 4, 7]
for node in nodes:
	cur.next = ListNode(node)
	cur = cur.next

new_head = sol.oddEvenList(head)
vals = [2, 3, 6, 7, 1, 5, 4]
for val in vals:
	assert val == new_head.val
	new_head = new_head.next
