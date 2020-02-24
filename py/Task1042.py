from typing import List


class Solution:
    def gardenNoAdj(self, N: int, paths: List[List[int]]) -> List[int]:
        adjlist = [[] for _ in range(N+1)]
        res = [None]*(N+1)
        for i, j in paths:
            adjlist[i].append(j)
            adjlist[j].append(i)
        candidate = {1, 2, 3, 4}
        for i in range(1, N+1):
            res[i] = (candidate-{res[j] for j in adjlist[i]}).pop()
        return res[1:]


N = 3
paths = [[1, 2], [2, 3], [3, 1]]
so = Solution()
so.gardenNoAdj(N, paths)
