from math import inf


def coinChange(coins, amount):
	if not amount:
		return 0

	dp = [[inf] * (amount + 1)] + [[0] * (amount + 1) for i in range(len(coins))]

	for coin_idx in range(1, len(coins) + 1):
		for cur_sum in range(1, amount + 1):
			if cur_sum-coins[coin_idx-1] >= 0:
				prev_v, new_v = dp[coin_idx-1][cur_sum], dp[coin_idx][cur_sum-coins[coin_idx-1]] + 1
				dp[coin_idx][cur_sum] = min(prev_v, new_v)
			else:
				dp[coin_idx][cur_sum] =  dp[coin_idx-1][cur_sum]
	

	return dp[-1][-1] if dp[-1][-1] != inf else -1