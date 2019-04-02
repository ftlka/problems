from solution import removeDuplicates


original = [1, 1, 1, 2, 2, 3]
elems = removeDuplicates(original)
assert elems == 5
assert original[:5] == [1, 1, 2, 2, 3]

original = [0, 0, 1, 1, 1, 1, 2, 3, 3]
elems = removeDuplicates(original)
assert elems == 7
assert original[:7] == [0, 0, 1, 1, 2, 3, 3]

original = [0, 1, 2]
elems = removeDuplicates(original)
assert elems == 3
assert original == [0, 1, 2]

original = []
elems = removeDuplicates(original)
assert elems == 0
assert original == []


original = [0, 0, 0, 1, 1, 1, 2]
elems = removeDuplicates(original)
assert elems == 5
assert original[:5] == [0, 0, 1, 1, 2]


original = [0, 0, 0, 0, 0, 1, 1, 1, 1, 2]
elems = removeDuplicates(original)
assert elems == 5
assert original[:5] == [0, 0, 1, 1, 2]
