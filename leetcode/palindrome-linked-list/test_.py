from solution import Solution, ListNode


def create_linked_list(l):
	root = ListNode(0)
	start = ListNode(l[0])
	root.next = start
	for el in l[1:]:
		start.next = ListNode(el)
		start = start.next
	return root.next

s = Solution()
# basic tests
assert not s.isPalindrome(create_linked_list([1, 2]))

assert s.isPalindrome(create_linked_list([1, 2, 2, 1]))

assert s.isPalindrome(create_linked_list([1, 2, 3, 2, 1]))

assert not s.isPalindrome(create_linked_list([1, 2, 3]))
