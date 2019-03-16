def countBits(num):
    nums = [0] * (num + 1)
    current_pow = 1

    for i in range(1, num + 1):
        if i == current_pow:
            current_pow *= 2
            nums[i] = 1
        else:
            nums[i] = nums[i - int(current_pow / 2)] + 1

    return nums
