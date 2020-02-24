class Solution:
    # # 1，brute force 超时
    # def minCut(self, s: str) -> int:
    #     def isPalindrome(s):
    #         left, right = 0, len(s)-1
    #         while left < right:
    #             if s[left] != s[right]:
    #                 return False
    #             left += 1
    #             right -= 1
    #         return True
    #     if isPalindrome(s):
    #         return 0
    #     res = len(s)-1
    #     for i in range(len(s)-1):
    #         if isPalindrome(s[0:i+1]):
    #             res = min(1+self.minCut(s[i+1:]), res)
    #     return res

    # # dp 预处理是否回文
    # def minCut2(self, s: str) -> int:
    #     l = len(s)
    #     if l < 2:
    #         return 0
    #     dp = [[False]*l for _ in range(l)]
    #     for j in range(l):
    #         for i in range(j+1):
    #             dp[i][j] = True if s[i] == s[j] and (
    #                 j-i <= 1 or dp[i+1][j-1]) else False

    #     def helper(beg):
    #         if dp[beg][-1]:
    #             return 0
    #         res = l-beg-1
    #         for i in range(beg, l-1):
    #             if dp[beg][i]:
    #                 res = min(1+helper(i+1), res)
    #         return res
    #     return helper(0)

    # # dp 预处理是否回文 + 记忆化
    # def minCut3(self, s: str) -> int:
    #     l = len(s)
    #     if l < 2:
    #         return 0
    #     dp = [[False]*l for _ in range(l)]
    #     for j in range(l):
    #         for i in range(j+1):
    #             dp[i][j] = True if s[i] == s[j] and (
    #                 j-i <= 1 or dp[i+1][j-1]) else False
    #     map = {}

    #     def helper(beg):
    #         if beg in map:
    #             return map[beg]
    #         if dp[beg][-1]:
    #             map[beg] = 0
    #             return 0
    #         res = l-beg-1
    #         for i in range(beg, l-1):
    #             if dp[beg][i]:
    #                 res = min(1+helper(i+1), res)
    #         map[beg] = res
    #         return res
    #     return helper(0)

    # # dp 预处理是否回文 + 递推
    # def minCut4(self, s: str) -> int:
    #     l = len(s)
    #     if l < 2:
    #         return 0
    #     check = [[False]*l for _ in range(l)]
    #     for j in range(l):
    #         for i in range(j+1):
    #             check[i][j] = True if s[i] == s[j] and (
    #                 j-i <= 1 or check[i+1][j-1]) else False

    #     dp = [i for i in range(l)]

    #     for i in range(1, l):
    #         if check[0][i]:
    #             dp[i] = 0
    #             continue
    #         for j in range(1, i+1):
    #             if check[j][i]:
    #                 dp[i] = min(1+dp[j-1], dp[i])
    #     return dp[-1]

    # 中心扩展 + 递推
    def minCut(self, s: str) -> int:
        if s == s[::-1]:
            return 0
        l = len(s)
        dp = [i for i in range(l)]
        for i in range(l):
            # odd
            left = right = i
            while left >= 0 and right < l and s[left] == s[right]:
                dp[right] = 0 if left == 0 else min(dp[left-1]+1, dp[right])
                left -= 1
                right += 1
            # even
            left, right = i, i+1
            while left >= 0 and right < l and s[left] == s[right]:
                dp[right] = 0 if left == 0 else min(dp[left-1]+1, dp[right])
                left -= 1
                right += 1
        return dp[-1]
