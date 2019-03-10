from solution import Trie

#basic tests
trie = Trie()

trie.insert('apple')
assert trie.search('apple')
assert not trie.search('app')
assert trie.startsWith('app')
trie.insert('app') 
assert trie.search('app')
