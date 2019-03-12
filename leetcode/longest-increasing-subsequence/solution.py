def lengthOfLIS(nums):
	if not nums:
		return 0

	maximum = 1
	len_ar = [1] * len(nums)

	for i in range(1, len(nums)):
		for j in range(0, i):
			if nums[j] < nums[i]:
				len_ar[i] = max(len_ar[j] + 1, len_ar[i])
				if len_ar[i] > maximum:
					maximum = len_ar[i]

	return maximum
        