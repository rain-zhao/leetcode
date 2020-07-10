from typing import List


class Trie:
    def __init__(self):
        self.next = [None] * 26
        self.isEnd = False

    def insert(self, word: str):
        curPos = self
        word = word[::-1]
        for c in word:
            idx = ord(c) - 97
            if not curPos.next[idx]:
                curPos.next[idx] = Trie()
            curPos = curPos.next[idx]
        curPos.isEnd = True


class Solution:
    # dp & trie (后缀)
    def respace(self, dictionary: List[str], sentence: str) -> int:
        if not sentence:
            return 0
        l = len(sentence)
        if not dictionary:
            return l
        root = Trie()
        for word in dictionary:
            root.insert(word)

        # define and init
        dp = [0] * (l+1)
        for i in range(l):
            dp[i+1] = dp[i] + 1
            curPos = root
            for j in range(i, -1, -1):
                idx = ord(sentence[j]) - 97
                if not curPos.next[idx]:
                    break
                curPos = curPos.next[idx]
                if curPos.isEnd:
                    dp[i+1] = min(dp[i+1], dp[j])
                    if dp[i+1] == 0:
                        break
        return dp[-1]


dictionary = ["looked", "just", "like", "her", "brother"]
sentence = "jesslookedjustliketimherbrother"


# dictionary = ["abc", ]
# sentence = "dabc"
obj = Solution()
print(obj.respace(dictionary, sentence))
