from collections import Counter


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        return list(Counter(t)-Counter(s))[0]


s = "abcd"
t = "abcde"
obj = Solution()
print(obj.findTheDifference(s, t))
