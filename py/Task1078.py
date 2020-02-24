from typing import List


class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        text = text.split()
        return [trd for fst, sed, trd in zip(text, text[1:], text[2:]) if fst == first and sed == second]


text = "alice is a good girl she is a good student"
first = "a"
second = "good"
so = Solution()
print(so.findOcurrences(text, first, second))
