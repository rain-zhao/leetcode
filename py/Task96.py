class Solution:
    # recursion 减治
    def numTrees(self, n: int) -> int:
        if n < 2:
            return 1
        res = 0
        for i in range(n):
            res += self.numTrees(i) * self.numTrees(n - i - 1)
        return res

    # recursion + memo
    def numTrees2(self, n: int) -> int:
        memo = {}

        def countTrees(n: int) -> int:
            if n < 2:
                return 1
            if n in memo:
                return memo[n]
            res = 0
            for i in range(n):
                res += countTrees(i) * countTrees(n - i - 1)
            memo[n] = res
            return res
        return countTrees(n)

    # dp
    def numTrees3(self, n: int) -> int:
        if n < 2:
            return 1
        dp = [1] + [0] * n
        for i in range(1, n + 1):
            res = 0
            for j in range(i):
                res += dp[j] * dp[i - j - 1]
            dp[i] = res
        return dp[-1]


n = 19
obj = Solution()
print(obj.numTrees3(n))
