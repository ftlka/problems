def search(nums, target):
    lo = 0
    hi = len(nums) - 1

    while lo <= hi:
        mid = int((hi + lo) / 2)
        if target == nums[mid]:
            return mid
        if lo == hi:
            return lo if target == nums[lo] else -1

        if nums[lo] <= nums[mid]:
            # left half is sorted 
            if nums[lo] <= target < nums[mid]:
                # if target is in this half we focus on it
                hi = mid - 1
            else:
                # otherwise move over to another half
                lo = mid + 1
        else:
            # left half is not sorted
            if nums[mid] < target <= nums[hi]:
                # target will be in the right half
                lo = mid + 1
            else:
                hi = mid - 1

    return -1
