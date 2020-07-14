from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return 0
        l = len(triangle)
        dp = triangle[-1][:]
        for i in range(l - 2, -1, -1):
            for j in range(i + 1):
                dp[j] = min(dp[j], dp[j+1])+triangle[i][j]
        return dp[0]


triangle = [
    [2],
    [3, 4],
    [6, 5, 7],
    [4, 1, 8, 3]
]

obj = Solution()
print(obj.minimumTotal(triangle))
