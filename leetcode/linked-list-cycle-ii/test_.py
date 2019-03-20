from solution import ListNode, Solution


s = Solution()

# test 1
root = cur = ListNode(3)
loop_node = cur.next = ListNode(2)
cur = cur.next
cur.next = ListNode(0)
cur = cur.next
cur.next = ListNode(-4)
cur = cur.next
cur.next = loop_node

assert s.detectCycle(root).val == 2


# test 2
root = cur = ListNode(1)
cur.next = ListNode(2)
cur.next.next = cur

assert s.detectCycle(root).val == 1


# test 3
root = ListNode(1)

assert not s.detectCycle(root)


# test 4
assert not s.detectCycle(None)


# test 5
root = cur = ListNode(1)
for i in range(2, 6):
	cur.next = ListNode(i)
	cur = cur.next

assert not s.detectCycle(root)

