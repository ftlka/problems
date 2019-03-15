def mincostTickets(days, costs):
		dp = [0] * 365

		for i in range(365):
			if i + 1 not in days:
				dp[i] = dp[i-1]
			else:
				one_day = costs[0] if i < 1 else dp[i-1] + costs[0]
				seven_days = costs[1] if i < 7 else dp[i-7] + costs[1]
				thirty_days = costs[2] if i < 30 else dp[i-30] + costs[2]
				dp[i] = min(one_day, seven_days, thirty_days)
		
		return dp[days[-1]-1]
