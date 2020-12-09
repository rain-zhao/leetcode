class Solution:
    # dp + 压缩空间
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [0] * m
        dp[0] = 1
        for _ in range(n):
            for i in range(1, m):
                dp[i] += dp[i-1]
        return dp[-1]


m = 3
n = 2
obj = Solution()
print(obj.uniquePaths(m, n))
