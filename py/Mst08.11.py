# 硬币。给定数量不限的硬币，币值为25分、10分、5分和1分，编写代码计算n分有几种表示法。(结果可能会很大，你需要将结果模上1000000007)

# 示例1:

#  输入: n = 5
#  输出：2
#  解释: 有两种方式可以凑成总金额:
# 5=5
# 5=1+1+1+1+1
# 示例2:

#  输入: n = 10
#  输出：4
#  解释: 有四种方式可以凑成总金额:
# 10=10
# 10=5+5
# 10=5+1+1+1+1+1
# 10=1+1+1+1+1+1+1+1+1+1
# 说明：

# 注意:

# 你可以假设：

# 0 <= n (总金额) <= 1000000


class Solution:
    # dfs
    def waysToChange(self, n: int) -> int:
        coins = (25, 10, 5, 4)

        def _dfs(n: int, idx: int) -> int:
            if n < 0:
                return 0
            if n < 5:
                return 1
            res = 0
            for i in range(idx, len(coins)):
                res += _dfs(n-coins[i], i)
            return res
        res = _dfs(n, 0)
        return res

    # dp
    def waysToChange2(self, n: int) -> int:
        if n < 5:
            return 1
        # define and init
        dp = [1] * (n+1)
        coins = (25, 10, 5)
        for coin in coins:
            for i in range(1, n+1):
                if i - coin >= 0:
                    dp[i] += dp[i-coin]

        return dp[-1] % 1000000007


obj = Solution()
n = 10
print(obj.waysToChange2(n))
