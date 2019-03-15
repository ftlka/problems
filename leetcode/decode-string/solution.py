def decodeString(s):
    if not s:
        return
    ar = []
    i = 0
    while i < len(s):
        if s[i].isdigit():
            if i > 0 and s[i-1].isalpha():
                ar.append('\'')
            ar.append('+')
            num = s[i]
            while s[i+1].isdigit():
                i += 1
                num += s[i]
            ar.append(num)

        elif s[i] == '[':
            ar.append('*(')

        elif s[i] == ']':
            if i > 0 and s[i-1].isalpha():
                ar.append('\'') 
            ar.append(')')

        else:
            if i == 0:
                ar.append('\'')
            elif ar[-1][-1] == '(':
                ar.append('\'')
            if i > 0 and ar[-1][-1] == ')':
                ar.append('+\'')
            ar.append(s[i])
            if i == len(s) - 1:
                ar.append('\'')

        i += 1

    return eval(''.join(ar))
