from solution import LFUCache


# test 1
cache = LFUCache(2)

cache.put(1, 1)
cache.put(2, 2)
assert cache.get(1) == 1
cache.put(3, 3)
assert cache.get(2) == -1
assert cache.get(3) == 3
cache.put(4, 4)
assert cache.get(1) == -1
assert cache.get(3) == 3
assert cache.get(4) == 4


# test 2
cache = LFUCache(0)
cache.put(0, 0)
assert cache.get(0) == -1


# test 3
cache = LFUCache(3)

cache.put(2, 2)
cache.put(1, 1)
assert cache.get(2) == 2
assert cache.get(1) == 1
assert cache.get(2) == 2
cache.put(3, 3)
cache.put(4, 4)
assert cache.get(3) == -1
assert cache.get(2) == 2
assert cache.get(1) == 1
assert cache.get(4) == 4


# test 4
cache = LFUCache(3)
cache.put(1, 1)
assert cache.get(1) == 1
assert cache.get(1) == 1
assert cache.get(1) == 1
cache.put(2, 2)
cache.put(3, 3)
cache.put(1, 2)
assert cache.get(2) == 2
assert cache.get(3) == 3
cache.put(4, 4)
assert cache.get(1) == 2


# test 5
cache = LFUCache(2)
cache.put(2, 1)
cache.put(2, 2)
assert cache.get(2) == 2
cache.put(1, 1)
cache.put(4, 1)
assert cache.get(2) == 2
