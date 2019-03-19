from solution import ListNode, Solution


s = Solution()

# test 1
root = cur = ListNode(1)
for node in range(2, 6):
	cur.next = ListNode(node)
	cur = cur.next

assert s.middleNode(root).val == 3


# test 2
root = cur = ListNode(1)
for node in range(2, 7):
	cur.next = ListNode(node)
	cur = cur.next

assert s.middleNode(root).val == 4


# test 3
root = ListNode(1)
root.next = ListNode(2)

assert s.middleNode(root).val == 2


# test 4
assert not s.middleNode(None)


# test 5
assert s.middleNode(ListNode(1)).val == 1
