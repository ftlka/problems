from solution import ListNode, Solution


s = Solution()

# test 1
l = cur = ListNode(1)
for i in range(2, 6):
	cur.next = ListNode(i)
	cur = cur.next

result = s.reverseBetween(l, 2, 4)
expected = [1, 4, 3, 2, 5]
for el in expected:
	assert result.val == el
	result = result.next


# test 2
l = ListNode(3)
l.next = ListNode(5)

result = s.reverseBetween(l, 1, 1)
expected = [3, 5]

for el in expected:
	assert result.val == el
	result = result.next


# test 3
l = ListNode(3)
l.next = ListNode(5)

result = s.reverseBetween(l, 2, 2)
expected = [3, 5]

for el in expected:
	assert result.val == el
	result = result.next


# test 4
l = ListNode(3)
l.next = ListNode(5)

result = s.reverseBetween(l, 1, 2)
expected = [5, 3]

for el in expected:
	assert result.val == el
	result = result.next


# test 5
l = ListNode(1)
l.next = ListNode(2)

result = s.reverseBetween(l, 1, 2)
expected = [2, 1]

for el in expected:
	assert result.val == el
	result = result.next


# test 6
l = ListNode(1)
l.next = ListNode(2)
l.next.next = ListNode(3)

result = s.reverseBetween(l, 1, 3)
expected = [3, 2, 1]
for el in expected:
	assert result.val == el
	result = result.next


# test 7
root = l = ListNode(1)
for i in range(2, 7):
	l.next = ListNode(i)
	l = l.next

result = s.reverseBetween(root, 5, 6)
expected = [1, 2, 3, 4, 6, 5]
for el in expected:
	assert result.val == el
	result = result.next
