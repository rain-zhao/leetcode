from typing import Dict


class WordDictionary:
    def __init__(self):
        self.root = {}

    def addWord(self, word: str) -> None:
        cur = self.root
        for char in word:
            if char not in cur:
                cur[char] = {}
            cur = cur[char]
        cur[0] = True

    # def search(self, word: str) -> bool:
    #     return self.__dfs(self.root, word)

    # def __dfs(self, root: Dict, word: str) -> bool:
    #     if not word:
    #         return 0 in root
    #     for idx, char in enumerate(word):
    #         if char == '.':
    #             for key in root:
    #                 if key == 0:
    #                     continue
    #                 if self.__dfs(root[key], word[idx+1:]):
    #                     return True
    #             return False
    #         elif char not in root:
    #             return False
    #         else:
    #             root = root[char]
    #     return 0 in root

    def search(self, word: str) -> bool:
        def dfs(root: Dict, word: str) -> bool:
            if not word:
                return 0 in root
            char = word[0]
            if char == '.':
                return sum([1 if dfs(root[key], word[1:]) else 0 for key in root if key != 0])
            elif char in root:
                return dfs(root[char], word[1:])
            else:
                return False
        return dfs(self.root, word)

        # Your WordDictionary object will be instantiated and called as such:
obj = WordDictionary()
obj.addWord("bad")
obj.addWord("dad")
obj.addWord("mad")
print(obj.search("b.."))
