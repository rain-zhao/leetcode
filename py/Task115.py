# 给定一个字符串 S 和一个字符串 T，计算在 S 的子序列中 T 出现的个数。

# 一个字符串的一个子序列是指，通过删除一些（也可以不删除）字符且不干扰剩余字符相对位置所组成的新字符串。（例如，"ACE" 是 "ABCDE" 的一个子序列，而 "AEC" 不是）

# 示例 1:

# 输入: S = "rabbbit", T = "rabbit"
# 输出: 3
# 解释:

# 如下图所示, 有 3 种可以从 S 中得到 "rabbit" 的方案。
# (上箭头符号 ^ 表示选取的字母)

# rabbbit
# ^^^^ ^^
# rabbbit
# ^^ ^^^^
# rabbbit
# ^^^ ^^^
# 示例 2:

# 输入: S = "babgbag", T = "bag"
# 输出: 5
# 解释:

# 如下图所示, 有 5 种可以从 S 中得到 "bag" 的方案。
# (上箭头符号 ^ 表示选取的字母)

# babgbag
# ^^ ^
# babgbag
# ^^    ^
# babgbag
# ^    ^^
# babgbag
#   ^  ^^
# babgbag
#     ^^^


class Solution:
    # 1.brute force,recursion
    def numDistinct(self, s: str, t: str) -> int:
        ls, lt = len(s), len(t)
        self.cnt = 0

        def _helper(l1, l2):
            if l2 == lt:
                self.cnt += 1
                return
            if l1 == ls:
                return
            if s[l1] == t[l2]:
                _helper(l1+1, l2+1)
            _helper(l1+1, l2)
        _helper(0, 0)

        return self.cnt

    # dp
    def numDistinct2(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        # define and init
        dp = [[0] * (n+1) for _ in range(m+1)]
        for i in range(m+1):
            dp[i][0] = 1
        # iter
        for i in range(m):
            for j in range(n):
                if s[i] == t[j]:
                    dp[i+1][j+1] += dp[i][j]
                dp[i+1][j+1] += dp[i][j+1]
        return dp[-1][-1]

    # dp + compress
    def numDistinct3(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        dp = [1] + [0] * n
        for i in range(m):
            for j in range(n-1, -1, -1):
                if s[i] == t[j]:
                    dp[j+1] += dp[j]
        return dp[-1]


S = "rabbbit"
T = "rabbit"
obj = Solution()
print(obj.numDistinct3(S, T))
