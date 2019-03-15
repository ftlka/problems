from solution import ListNode, Solution


s = Solution()

ar1 = [1, 2, 4]
ar2 = [1, 3, 4]

l1 = c1 = ListNode(1)
l2 = c2 = ListNode(1)
for i in range(1, 3):
	c1.next = ListNode(ar1[i])
	c1 = c1.next
	c2.next = ListNode(ar2[i])
	c2 = c2.next

merged = s.mergeTwoLists(l1, l2)

expected_res = [1, 1, 2, 3, 4, 4]
i = 0
while merged:
	assert merged.val == expected_res[i]
	merged = merged.next
	i += 1
