from collections import Counter


def leastInterval(tasks, n):
    c = Counter(tasks)
    res = []
    while len(c):
        i = n + 1
        for task, amount_left in c.most_common():
            res.append(task)
            c.subtract(task)
            if c[task] <= 0:
                del c[task]

            i -= 1
            if i == 0 and len(c):
                res += ['Idle'] * i
                break
        else:
            if i > 0 and len(c):
                res += ['Idle'] * i

    return len(res)
