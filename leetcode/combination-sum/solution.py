from collections import deque, namedtuple


def combinationSum(candidates, target):
    res = []
    Perm = namedtuple('Perm', ['cur_sum', 'ar', 'min_i'])
    stack = deque()
    for i, candidate in enumerate(candidates):
        if candidate <= target:
            stack.append(Perm(candidate, [candidate], i))
    while stack:
        cur_perm = stack.pop()
        if cur_perm.cur_sum == target:
            res.append(cur_perm.ar)
        else:
            for i in range(cur_perm.min_i, len(candidates)):
                if candidates[i] + cur_perm.cur_sum <= target:
                    stack.append(Perm(candidates[i] + cur_perm.cur_sum, cur_perm.ar + [candidates[i]], max(i, cur_perm.min_i)))

    return res
