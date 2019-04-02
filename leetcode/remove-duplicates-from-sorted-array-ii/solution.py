def removeDuplicates(nums):
    if not nums:
        return 0
    cur_val = nums[0]
    cur_counter = 1
    cur_swap_idx = -1

    for i in range(1, len(nums)):
        if nums[i] == cur_val:
            if cur_counter >= 2:
                if cur_swap_idx == -1:
                    cur_swap_idx = i
            else:
                if cur_swap_idx != -1:
                    nums[cur_swap_idx] = nums[i]
                    cur_swap_idx += 1
            cur_counter += 1
        else:
            cur_counter = 1
            cur_val = nums[i]
            if cur_swap_idx != -1:
                nums[cur_swap_idx] = nums[i]
                cur_swap_idx += 1

    return len(nums) if cur_swap_idx == -1 else cur_swap_idx
        