from collections import namedtuple


def PredictTheWinner(nums):
	Cell = namedtuple('Cell', ['first', 'second'])
	dp = [[0] * len(nums) for num in nums]
	
	for i, num in enumerate(nums):
		dp[i][i] = Cell(num, 0)

	for size in range(1, len(nums)):
		for i in range(len(nums) - size):
			j = i + size
			if nums[i] + dp[i+1][j].second >= nums[j] + dp[i][j-1].second:
				first = nums[i] + dp[i+1][j].second
				second = dp[i+1][j].first
			else:
				first = nums[j] + dp[i][j-1].second
				second = dp[i][j-1].first
			dp[i][j] = Cell(first, second)
	

	return dp[0][-1].first >= dp[0][-1].second
