from collections import Counter


class Solution:
    # recursion
    def isScramble(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        if Counter(s1) != Counter(s2):
            return False
        l = len(s1)
        for i in range(1, l):
            if self.isScramble(s1[0:i], s2[0:i]) and self.isScramble(s1[i:], s2[i:]) \
                    or self.isScramble(s1[0:i], s2[l-i:]) and self.isScramble(s1[i:], s2[0:l-i]):
                return True
        return False
    # recursion + 记忆化
    def isScramble2(self, s1: str, s2: str) -> bool:
        map = {}
        def helper(s1:str,s2:str)->bool:
            if s1 == s2:
                return True
            key = s1+','+s2
            if key in map:
                return map[key]
            if Counter(s1) != Counter(s2):
                map[key] = False
                return False
            l = len(s1)
            for i in range(1, l):
                if self.isScramble(s1[0:i], s2[0:i]) and self.isScramble(s1[i:], s2[i:]) \
                        or self.isScramble(s1[0:i], s2[l-i:]) and self.isScramble(s1[i:], s2[0:l-i]):
                    map[key] = True
                    return True
            return False
        return helper(s1,s2)
    # dp
    def isScramble3(self, s1: str, s2: str) -> bool:


s1 = "great"
s2 = "rgeat"
so = Solution()
print(so.isScramble(s1,s2))