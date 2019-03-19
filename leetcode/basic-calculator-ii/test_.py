from solution import calculate


assert calculate('3+2*2') == 7

assert calculate(' 3/2 ') == 1

assert calculate(' 3+5 / 2 ') == 5

assert calculate('14+16') == 30

assert calculate('0-1') == -1
