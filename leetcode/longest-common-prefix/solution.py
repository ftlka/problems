def longestCommonPrefix(strs):
    if not strs:
        return ''

    res = ''
    i = 0

    while True:
        for idx, word in enumerate(strs):
            if i >= len(word):
                return res[:i]

            if idx == 0:
                res += word[i]
            elif res[i] != word[i]:
                return res[:-1]

        i += 1

    return res
