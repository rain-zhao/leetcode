# 给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。

# 示例 1:

# 输入: coins = [1, 2, 5], amount = 11
# 输出: 3
# 解释: 11 = 5 + 5 + 1
# 示例 2:

# 输入: coins = [2], amount = 3
# 输出: -1
# 说明:
# 你可以认为每种硬币的数量是无限的。

from typing import List


class Solution:
    # dp
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not amount:
            return 0
        # 去掉比amount大的硬币
        coins = [coin for coin in coins if coin <= amount]
        if not len(coins):
            return -1
        # define and init
        # dp[i] 表示amount = i 的总金额凑到最小的硬币数，-1表示不可能
        dp = [-1 for _ in range(amount+1)]
        dp[0] = 0

        for i in range(min(coins), amount+1):
            for coin in coins:
                if dp[i-coin] != -1:
                    dp[i] = min(dp[i], dp[i-coin]+1) \
                        if dp[i] != -1 else dp[i-coin]+1
        return dp[-1]

    # dp 2 另一种遍历方法
    def coinChange2(self, coins: List[int], amount: int) -> int:  
        if not amount:
            return 0
        if not len(coins):
            return -1
        # define and init
        # dp[i] 表示amount = i 的总金额凑到最小的硬币数，-1表示不可能
        dp = [-1 for _ in range(amount+1)]
        dp[0] = 0
        for i in range(amount+1):
            if dp[i] == -1:
                continue
            for coin in coins:
                if i + coin <= amount:
                    dp[i+coin] = min(dp[i]+1,dp[i+coin]) \
                        if dp[i+coin] != -1 else dp[i]+1 
        return dp[-1]


coins = [1, 2, 5]
amount = 11

obj = Solution()
print(obj.coinChange2(coins, amount))
