from solution import decodeString

assert decodeString('3[a]2[bc]') == 'aaabcbc'

assert decodeString('3[a2[c]]') == 'accaccacc'

assert decodeString('2[abc]3[cd]ef') == 'abcabccdcdcdef'

assert decodeString('a2[abc]3[cd]ef') == 'aabcabccdcdcdef'

assert decodeString('12[a]') == 12 * 'a'

assert decodeString('b3[a2[c]a]d') == 'b' + 3 * 'acca' + 'd'

assert decodeString('2[1[y]1[f]]') == 2 * 'yf'

assert decodeString('4[2[jk]e1[f]]') ==  4 * ( 2 * 'jk' + 'e' + 'f')

assert decodeString('2[2[2[j]]]') == 8 * 'j'

assert decodeString('') == ''
