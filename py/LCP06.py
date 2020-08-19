from typing import List


class Solution:
    def minCount(self, coins: List[int]) -> int:
        # res = 0
        # for coin in coins:
        #     res += (coin+1) >> 1
        # return res
        return sum((coin+1) >> 1 for coin in coins)
