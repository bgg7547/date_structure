
class TireNode:
    def __init__(self):
        self.data = {}
        self.is_word = False
    def __repr__(self):
        return str(self.data)
class Tire:
    def __init__(self):
        self.root = TireNode()

    # 插入
    def insert(self,word):
        node = self.root
        for char in word:
            child = node.data.get(char)
            if child is None:
                node.data[char] = TireNode()
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

    # 前缀
    def prefix(self,prefix):
        node = self.root
        for char in prefix:
            node = node.data.get(char)
            if not node:
                return False
        return True

tire = Tire()
tire.insert('something')
tire.insert('somewhere')
print(tire.root.data)
print(tire.search("some"))
print(tire.prefix("some"))
