from solution import subsets


def check_eq(a, b):
	if len(a) != len(b):
		return False
	for subset in a:
		if subset not in b:
			return False
	return True


# basic tests
nums = [1, 2, 3]
expected_res = [
	[3],
  	[1],
  	[2],
  	[1, 2, 3],
  	[1, 3],
  	[2, 3],
  	[1, 2],
  	[]
]
assert check_eq(subsets(nums), expected_res)


nums = [1, 2]
expected_res = [
  	[1],
  	[2],
  	[1, 2],
  	[]
]
assert check_eq(subsets(nums), expected_res)


nums = [1]
expected_res = [
  	[1],
  	[]
]
assert check_eq(subsets(nums), expected_res)


# empty list
assert subsets([]) == [[]]
