# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

# 示例 1：

# 输入: "babad"
# 输出: "bab"
# 注意: "aba" 也是一个有效答案。
# 示例 2：

# 输入: "cbbd"
# 输出: "bb"


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        res = s[0]
        l = len(s)
        dp = [[False]*l for _ in range(l)]
        for i in range(l):
            dp[i][i] = True
        for i in range(l-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                res = s[i:i+2]
        for k in range(2, l):
            for i in range(l-k):
                j = i + k
                if dp[i+1][j-1] and s[i] == s[j]:
                    dp[i][j] = True
                    if k+1 > len(res):
                        res = s[i:j+1]
        return res

    def longestPalindrome2(self, s: str) -> str:
        if len(s) <= 1:
            return s
        res = s[0]
        l = len(s)
        dp = [[False]*l for _ in range(l)]

        for k in range(l):
            for i in range(l-k):
                j = i + k
                if s[i] == s[j] and (j-i < 2 or dp[i+1][j-1]):
                    dp[i][j] = True
                    if k+1 > len(res):
                        res = s[i:j+1]
        return res

# 中心拓展
    def longestPalindrome3(self, s: str) -> str:
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


s = "babad"
so = Solution()
print(so.longestPalindrome3(s))
