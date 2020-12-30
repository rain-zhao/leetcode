from typing import List


class Solution:
    # dp
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        # dp(i,j,k) = 第i天，j=1持有,交易了k次，。最大利润
        dp = [[[-10**3] * (k+1) for _ in range(2)] for _ in range(n+1)]
        # init
        for i in range(n+1):
            dp[i][0][0] = 0
        for i in range(1, n+1):
            for k in range(1, k+1):
                dp[i][0][k] = max(dp[i-1][1][k]+prices[i-1], dp[i-1][0][k])
                dp[i][1][k] = max(dp[i-1][0][k-1]-prices[i-1], dp[i-1][1][k])
        return max(dp[n][0])

    # dp + space compress
    def maxProfit2(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        hold, no_hold = [-10**3] * (k+1), [0] * (k+1)
        for i in range(n):
            for k in range(1, k+1):
                no_hold[k] = max(hold[k]+prices[i], no_hold[k])
                hold[k] = max(no_hold[k-1]-prices[i], hold[k])
        return max(no_hold)


k = 2
prices = [3, 2, 6, 5, 0, 3]
obj = Solution()
print(obj.maxProfit2(k, prices))
