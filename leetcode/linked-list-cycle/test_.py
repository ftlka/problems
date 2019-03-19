from solution import ListNode, Solution


s = Solution()

# tail connects to 2
head = cur = ListNode(3)
second = cur.next = ListNode(2)
cur, cur.next = cur.next, ListNode(0)
cur, cur.next = cur.next, ListNode(-4)
cur.next.next = second

assert s.hasCycle(head)


# tail connects to 1
head = cur = ListNode(1)
cur.next = ListNode(2)
cur.next.next = head

assert s.hasCycle(head)


# without cycle
head = cur = ListNode(1)
for i in range(2, 6):
	cur.next = ListNode(i)
	cur = cur.next

assert not s.hasCycle(head)


# empty
assert not s.hasCycle(None)


# one list node
cur = ListNode(5)
assert not s.hasCycle(cur) 


# cycle with one node
cur = ListNode(5)
cur.next = cur
assert s.hasCycle(cur)
