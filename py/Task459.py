class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        length = len(s)
        for i in range(1, length // 2 + 1):
            if not length % i:
                j = length // i
                if s[:i] * j == s:
                    return True
        return False

    def repeatedSubstringPattern2(self, s: str) -> bool:
        return s in (s+s)[1:-1]


s = "abab"
obj = Solution()
print(obj.repeatedSubstringPattern2(s))
