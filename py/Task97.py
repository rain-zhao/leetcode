# 给定三个字符串 s1, s2, s3, 验证 s3 是否是由 s1 和 s2 交错组成的。

# 示例 1:

# 输入: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
# 输出: true
# 示例 2:

# 输入: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
# 输出: false


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if not s1 or not s2:
            return s1+s2 == s3
        l1, l2 = len(s1), len(s2)

        # define and init
        dp = [[False]*(l2+1) for _ in range(l1+1)]
        dp[0][0] = True
        # each i == 0
        for j in range(1, l2+1):
            dp[0][j] = dp[0][j-1] and s2[j-1] == s3[j-1]
        for i in range(1, l1+1):
            dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1]
        for i in range(1, l1+1):
            for j in range(1, l2+1):
                dp[i][j] = dp[i][j-1] and s2[j-1] == s3[i+j -
                                                        1] or dp[i-1][j] and s1[i-1] == s3[i+j-1]

        return dp[-1][-1]


s1 = "db"
s2 = "b"
s3 = "cbb"
so = Solution()
print(so.isInterleave(s1, s2, s3))
