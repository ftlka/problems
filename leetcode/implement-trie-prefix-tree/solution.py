class Node:
    def __init__(self, val):
        self.val = val
        self.children = []


    def add_child(self, child):
        self.children.append(child)


class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node('*')
        

    def insert(self, word):
        """
        Inserts a word into the trie.
        """
        word += '*'
        cur_node = self.root
        for letter in word:
            for child in cur_node.children:
                if child.val == letter:
                    cur_node = child
                    break
            else:
                new_node = Node(letter)
                cur_node.children.append(new_node)
                cur_node = new_node        
        

    def search(self, word):
        """
        Returns if the word is in the trie.
        """
        word += '*'
        cur_node = self.root
        for letter in word:
            for child in cur_node.children:
                if child.val == letter:
                    cur_node = child
                    break
            else:
                return False
        return True
        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        cur_node = self.root
        for letter in prefix:
            for child in cur_node.children:
                if child.val == letter:
                    cur_node = child
                    break
            else:
                return False
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)