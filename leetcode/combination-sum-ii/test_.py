from solution import combinationSum2


def check_answ(ar, target, expected_res):
	res = combinationSum2(ar, target)
	assert len(res) == len(expected_res)
	for exp in expected_res:
		assert exp in res


check_answ([10, 1, 2, 7, 6, 1, 5], 8, [
	[1, 7],
	[1, 2, 5],
	[2, 6],
	[1, 1, 6]
])

check_answ([2, 5, 2, 1, 2], 5, [[1, 2, 2], [5]])

check_answ([2, 6, 7], 7, [[7]])

check_answ([2, 3, 5], 8, [[3, 5]])

check_answ([1, 1, 1], 3, [[1, 1, 1]])

check_answ([1, 2, 3], 4, [[1, 3]])

check_answ([], 10, [])
