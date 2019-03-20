def decodeAtIndex(S, K):
	str_len = 0
	for c in S:
		if c.isdigit():
			str_len *= int(c)
		else:
			str_len += 1
	for c in reversed(S):
		if K > str_len:
			K %= str_len
		if (K == 0 or K == str_len) and c.isalpha():
			return c
		

		if c.isdigit():
			str_len //= int(c)
		else:
			str_len -= 1
