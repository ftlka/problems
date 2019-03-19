from collections import deque


def get_cur_num(s, i):
    num = int(s[i])
    while i + 1 < len(s) and s[i + 1].isdigit():
        num = num * 10 + int(s[i + 1])
        i += 1
    return num, i


def calculate(s):
    s = ''.join(s.split())
    nums = deque()
    operations = deque()

    i = 0
    while i < len(s):
        if s[i].isdigit():
            num, i = get_cur_num(s, i)
            nums.append(num)
        else:
            if s[i] in ['+', '-']:
                operations.append(s[i])
            else:
                prev = nums.pop()
                op = s[i]
                next_num, i = get_cur_num(s, i + 1)
                if op == '*':
                    nums.append(prev * next_num)
                else:
                    nums.append(prev // next_num)
        i += 1

    res = nums.popleft()
    while nums:
        next_num = nums.popleft()
        operation = operations.popleft()
        if operation == '+':
            res += next_num
        else:
            res -= next_num

    return res
    