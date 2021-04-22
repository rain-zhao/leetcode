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


matrix = [[2,2,-1]]
k = 3
obj = Solution()
print(obj.maxSumSubmatrix(matrix, k))
