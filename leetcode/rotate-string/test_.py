from solution import rotateString


assert not rotateString('a', 'b')

assert not rotateString('ababab', 'abab')

assert rotateString('a', 'a')

assert rotateString('aa', 'aa')

assert rotateString('aaa', 'aaa')

assert rotateString('aaaa', 'aaaa')

assert rotateString('abcd', 'dabc')

assert rotateString('txyzk', 'xyzkt')

assert rotateString('txyzk', 'txyzk')

assert rotateString('abaaa', 'baaaa')

assert rotateString('baaaa', 'abaaa')

assert rotateString('abcde', 'abcde')

assert rotateString('abcde', 'eabcd')

assert rotateString('abcde', 'deabc')

assert rotateString('abcde', 'cdeab')

assert rotateString('abcde', 'bcdea')

assert rotateString('iqquydyvivwfvtgkfewecqlarygkqdxaejpfftuspeeomwvagnrdkozpztitulzxzuifmljudkjnzoeswjayjihpazilfcbpfhvv',
	'ydyvivwfvtgkfewecqlarygkqdxaejpfftuspeeomwvagnrdkozpztitulzxzuifmljudkjnzoeswjayjihpazilfcbpfhvviqqu')

assert rotateString('ydyvivwfvtgkfewecqlarygkqdxaejpfftuspeeomwvagnrdkozpztitulzxzuifmljudkjnzoeswjayjihpazilfcbpfhvviqqu',
	'iqquydyvivwfvtgkfewecqlarygkqdxaejpfftuspeeomwvagnrdkozpztitulzxzuifmljudkjnzoeswjayjihpazilfcbpfhvv')

