def rob(nums):
	if not nums:
		return 0

	two_step = 0
	one_step = nums[0]

	for i in range(2, len(nums) + 1):
		one_step, two_step = max(one_step, two_step + nums[i - 1]), one_step

	return one_step
        