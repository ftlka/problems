from math import inf

def nextPermutation(nums):
        total_len = len(nums)-1
        cur_idx = -1
        for i in range(total_len):
            if nums[total_len-i] > nums[total_len-i-1]:
                # if the next num is less we exit the loop and try to find next greater num
                cur_idx = total_len-i-1
                break

        if cur_idx == -1:
            nums.sort()
            return

        closest_greater = inf
        closest_i = -1
        for i in range(cur_idx+1, total_len+1):
            if nums[i] > nums[cur_idx] and nums[i] < closest_greater:
                closest_i = i
                closest_greater = nums[i]
        # now we swap cur_inx and closest greater number and then sort all other numbers after cur_idx
        nums[cur_idx], nums[closest_i] = nums[closest_i], nums[cur_idx]
        # sort from cur_idx+1 to the end
        nums[cur_idx+1:] = sorted(nums[cur_idx+1:])
