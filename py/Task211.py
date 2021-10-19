from typing import List


# 前缀树
class WordDictionary:

    def __init__(self):
        self.root = [None] * 26 + [False]

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            idx = ord(c) - 97
            if not cur[idx]:
                cur[idx] = [None] * 26 + [False]
            cur = cur[idx]
        cur[-1] = True

    def search(self, word: str) -> bool:
        def dfs(root: List, word: str) -> bool:
            if not root:
                return False
            if not word:
                return root[-1]
            c = word[0]
            idx = ord(c) - 97
            subWord = word[1:]
            if c != '.':
                return dfs(root[idx], subWord)
            return not not sum(dfs(r, subWord) for r in root[:-1])
        return dfs(self.root, word)


# ["WordDictionary","addWord","addWord","addWord","addWord","search","search","addWord","search","search","search","search","search","search"]
# [[],["at"],["and"],["an"],["add"],["a"],[".at"],["bat"],[".at"],["an."],["a.d."],["b."],["a.d"],["."]]
obj = WordDictionary()
obj.addWord("at")
obj.addWord("and")
obj.addWord("an")
obj.addWord("add")
print(obj.search("a"))
print(obj.search(".at"))
obj.addWord("bat")
print(obj.search(".at"))
print(obj.search("an."))
print(obj.search("a.d."))
print(obj.search("b."))
print(obj.search("a.d"))
print(obj.search("."))
