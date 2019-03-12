def maxProfit(prices):
	if not prices:
		return 0

	res = [0] * len(prices)
	minimum = prices[0]

	for i in range(1, len(prices)):
		res[i] = max(prices[i] - minimum, res[i - 1])
		minimum = min(minimum, prices[i])

	return res[-1]
