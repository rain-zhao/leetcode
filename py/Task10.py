class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p:
            return not s

        m = len(s)
        n = len(p)

        # define
        dp = [[False] * (n+1) for _ in range(m + 1)]

        # init
        dp[0][0] = True
        for i in range(2, n+1):
            if p[i - 1] == '*':
                dp[0][i] = dp[0][i-2]

        # loop
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                ss = s[i - 1]
                pp = p[j - 1]
                if pp == '.' or ss == pp:
                    dp[i][j] = dp[i - 1][j - 1]
                elif pp == '*':
                    dp[i][j] = dp[i][j - 2]
                    ppp = p[j - 2]
                    if ppp == '.' or ss == ppp:
                        dp[i][j] = dp[i][j] or dp[i - 1][j]
        return dp[-1][-1]


s = ""
p = ".*"
obj = Solution()
print(obj.isMatch(s, p))
