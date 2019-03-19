from solution import largestNumber


assert largestNumber([1]) == '1'

assert largestNumber([10, 2]) == '210'

assert largestNumber([3, 30, 34, 5, 9]) == '9534330'

assert largestNumber([0, 0, 0, 0]) == '0'

assert largestNumber([0, 0]) == '0'
