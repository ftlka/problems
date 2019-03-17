from collections import deque


def checkValidString(s):
    stack = deque()
    stack_with_stars = deque()

    for i, c in enumerate(s):
        if c == '(':
            stack.append(i)
        elif c == '*':
            stack_with_stars.append(i)
        else:
            if stack:
                stack.pop()
            elif stack_with_stars:
                stack_with_stars.pop()
            else:
                return False

    while stack:
        if not stack_with_stars:
            return False

        br = stack.pop()
        star = stack_with_stars.pop()
        # theres no closing bracket
        if br > star:
            return False

    return True
