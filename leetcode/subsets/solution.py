def subsets(nums):
    result = [[]]

    for num in nums:
        current_res = [r + [num] for r in result]
        result = result + current_res
    return result
