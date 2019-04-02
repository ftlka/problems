from solution import combinationSum


def check_answ(ar, target, expected_res):
	res = combinationSum(ar, target)
	for exp in expected_res:
		assert exp in res


check_answ([2, 3, 6, 7], 7, [[7], [2, 2, 3]])

check_answ([2, 6, 7], 7, [[7]])

check_answ([2, 3, 5], 8, [[2, 2, 2, 2], [2, 3, 3], [3, 5]])

check_answ([1], 3, [[1, 1, 1]])

check_answ([1, 2, 3], 4, [[1, 1, 1, 1], [1, 1, 2], [2, 2], [1, 3]])

check_answ([], 10, [])
