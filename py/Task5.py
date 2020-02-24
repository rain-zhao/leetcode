class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        res = s[0]
        l = len(s)
        dp = [[False]*l for _ in range(l)]
        for j in range(l):
            for i in range(j+1):
                if s[i] == s[j] and (j-i < 2 or dp[i+1][j-1]):
                    dp[i][j] = True
                    if j-i+1 > len(res):
                        res = s[i:j+1]
        return res
    def longestPalindrome2(self, s: str) -> str:
        if len(s) <= 1:
            return s
        beg, end = 0, 1
        l = len(s)
        for i in range(l-1):
            left = right = i
            while left >= 0 and right < l and s[left] == s[right]:
                left -= 1
                right += 1
            if right - left - 1 > end - beg:
                beg, end = left+1, right
            left, right = i, i+1
            while left >= 0 and right < l and s[left] == s[right]:
                left -= 1
                right += 1
            if right - left - 1 > end-beg:
                beg, end = left+1, right
        return s[beg: end]
