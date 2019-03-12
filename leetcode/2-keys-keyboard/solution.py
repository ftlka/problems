def minSteps(n):
	memo = [0] * (n + 1)

	for i in range(2, n + 1):
		memo[i] = i
		for j in range(i-1, 1, -1):
			if i % j == 0:
				memo[i] = int(memo[j] + i / j)
				break

	return memo[-1]