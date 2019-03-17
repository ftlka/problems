from solution import checkValidString


assert checkValidString('()')

assert checkValidString('(*)')

assert checkValidString('(*))')

assert checkValidString('((*)')

assert checkValidString('')

assert not checkValidString('(')

assert checkValidString('(*')

assert checkValidString('*')

assert not checkValidString('*(()')

assert checkValidString('()((*)(*)(**))()')
