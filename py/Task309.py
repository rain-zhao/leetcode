from typing import List


class Solution:
    # dp
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        l = len(prices)
        # define and init
        # dp[i][0,1,2] = 第i天 持有，可买，冻结期 的最高利润
        dp = [[0, 0, 0] for _ in range(l)]
        dp[0] = [-prices[0], 0, 0]
        for i in range(1, l):
            price = prices[i]
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] - price)
            dp[i][1] = max(dp[i-1][1], dp[i-1][2])
            dp[i][2] = dp[i-1][0] + price
        return max(dp[-1])

    # dp 压缩空间
    def maxProfit2(self, prices: List[int]) -> int:
        if not prices:
            return 0
        bought, canBuy, coolDown = -prices[0], 0, 0
        for price in prices[1:]:
            bought = max(bought, canBuy - price)
            canBuy = max(canBuy, coolDown)
            coolDown = bought + price
        return max(canBuy, coolDown)


obj = Solution()
price = [1, 2, 3, 0, 2]
print(obj.maxProfit(price))
