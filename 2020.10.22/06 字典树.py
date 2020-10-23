# 多层字典嵌套{'s': {'o': {'m': { 'w': {'h': {'e': {'r': {'e': {}}}}}}}}}}

class TrieNode:
    def __init__(self):
        self.data = {}
        self.is_word = False
    def __repr__(self):
        return str(self.data)

class Trie:
    def __init__(self):
        self.root = TrieNode()

    # 插入
    def insert(self,word):
        node = self.root
        for char in word:
            child = node.data.get(char)
            if child is None:
                node.data[char] = TrieNode()
            node = node.data[char]
        node.is_word = True

    # 查找
    def search(self,word):
        node = self.root
        for char in word:
            node = node.data.get(char)
            if not node:
                return False
        return node.is_word

    # 判断前缀
    def is_prefix(self,prefix):
        node = self.root
        for char in prefix:
            node = node.data.get(char)
            if not node:
                return False
        return True


trie = Trie()
trie.insert('something')
trie.insert("somewhere")
print(trie.root.data)
print(trie.is_prefix("something"))


