from typing import List
from sortedcontainers import SortedList


class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        res = -10**5
        for i in range(m):
            total = [0] * n
            for j in range(i, m):
                for p in range(n):
                    total[p] += matrix[j][p]

                sortedList = SortedList([0])
                s = 0
                for v in total:
                    s += v
                    idx = sortedList.bisect_left(s-k)
                    if idx < len(sortedList):
                        res = max(res, s-sortedList[idx])
                    sortedList.add(s)
        return res

    # dp
    def maxSumSubmatrix2(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        res = -10**5
        for i in range(1, m+1):
            for j in range(1, n+1):
                dp = [[0] * (n+1) for _ in range(m+1)]
                dp[i][j] = matrix[i-1][j-1]
                for p in range(i, m+1):
                    for q in range(j, n+1):
                        dp[p][q] = dp[p][q-1] + dp[p-1][q] - \
                            dp[p-1][q-1] + matrix[p-1][q-1]
                        if dp[p][q] <= k and dp[p][q] > res:
                            res = dp[p][q]
        return res


matrix = [[2, 2, -1]]
k = 3
obj = Solution()
print(obj.maxSumSubmatrix2(matrix, k))
