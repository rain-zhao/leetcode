# 在一个由 0 和 1 组成的二维矩阵内，找到只包含 1 的最大正方形，并返回其面积。

# 示例:

# 输入:

# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0

# 输出: 4

from typing import List


class Solution:
    # 原地dp
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        m = len(matrix)
        n = len(matrix[0])

        res = 0
        # define and init
        dp = [[0]*n for _ in range(m)]

        for i in range(m):
            dp[i][0] = int(matrix[i][0])
            if dp[i][0]:
                res = 1

        for i in range(n):
            dp[0][i] = int(matrix[0][i])
            if dp[0][i]:
                res = 1

        for i in range(1, m):
            for j in range(1, n):
                if '0' == matrix[i][j]:
                    continue
                dp[i][j] = min(dp[i-1][j],
                               dp[i][j-1],
                               dp[i-1][j-1]
                               ) + 1
                res = max(res, dp[i][j]**2)

        return res


obj = Solution()
matrix = [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"],
          ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]
print(obj.maximalSquare(matrix))
