from solution import longestCommonPrefix


assert longestCommonPrefix(['flower', 'flow', 'flight']) == 'fl'

assert longestCommonPrefix(['dog', 'racecar', 'car']) == ''

assert longestCommonPrefix(['aaa', 'aaa', 'aaa']) == 'aaa'

assert longestCommonPrefix([]) == ''

assert longestCommonPrefix(['aa', 'a']) == 'a'
