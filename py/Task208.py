
class Trie:

    def __init__(self):
        # first column represent isEndOfWord
        self.node = [None] * 27

    def insert(self, word: str) -> None:
        node = self.node
        for c in word:
            idx = ord(c) - 96
            if not node[idx]:
                node[idx] = [None] * 27
            node = node[idx]
        node[0] = True

    def search(self, word: str) -> bool:
        node = self.node
        for c in word:
            idx = ord(c) - 96
            if not node[idx]:
                return False
            node = node[idx]
        return not not node[0]

    def startsWith(self, prefix: str) -> bool:
        node = self.node
        for c in prefix:
            idx = ord(c) - 96
            if not node[idx]:
                return False
            node = node[idx]
        return True


# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert('apple')
print(obj.search('appl'))
print(obj.search('apple'))
print(obj.startsWith('appl'))
print(obj.startsWith('apple'))
print(obj.startsWith('applee'))
