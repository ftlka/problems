from solution import ListNode, Solution


s = Solution()

# test 1
# 1 -> 1 -> 2
root = cur = ListNode(1)
next_nodes = [1, 2]
for node in next_nodes:
	cur.next = ListNode(node)
	cur = cur.next

expected = [1, 2]
result = s.deleteDuplicates(root)
for val in expected:
	assert result.val == val
	result = result.next


# test 2
# 1 -> 1 -> 2 -> 3 -> 3
root = cur = ListNode(1)
next_nodes = [1, 2, 3, 3]
for node in next_nodes:
	cur.next = ListNode(node)
	cur = cur.next

expected = [1, 2, 3]
result = s.deleteDuplicates(root)
for val in expected:
	assert result.val == val
	result = result.next


# test 3
# 1 -> 1 -> 1 -> 1 -> 1
root = cur = ListNode(1)
next_nodes = [1, 1, 1, 1]
for node in next_nodes:
	cur.next = ListNode(node)
	cur = cur.next

expected = [1]
result = s.deleteDuplicates(root)
for val in expected:
	assert result.val == val
	result = result.next


# test 4
# no dups: 1 -> 2 -> 3 -> 4 -> 5
root = cur = ListNode(1)
next_nodes = [2, 3, 4, 5]
for node in next_nodes:
	cur.next = ListNode(node)
	cur = cur.next

expected = [1, 2, 3, 4, 5]
result = s.deleteDuplicates(root)
for val in expected:
	assert result.val == val
	result = result.next
