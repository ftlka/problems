from functools import cmp_to_key


def largestNumber(nums):
    res = [str(num) for num in nums]
    comp = lambda a, b: 1 if a + b < b + a else -1
    sorted_str = ''.join(sorted(res, key=cmp_to_key(comp)))

    # for zeros
    while sorted_str[0] == '0' and len(sorted_str) != 1:
        sorted_str = sorted_str[1:]

    return sorted_str