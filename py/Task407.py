from typing import List
import heapq


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        m, n = len(heightMap), len(heightMap[0])
        if m < 3 or n < 3:
            return 0

        res = 0
        visited = [[False] * n for _ in range(m)]
        heap = []
        direct = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        # put into priority queue
        for i in range(n):
            heapq.heappush(heap, [heightMap[0][i], 0, i])
            visited[0][i] = True
            heapq.heappush(heap, [heightMap[m-1][i], m-1, i])
            visited[m-1][i] = True
        for i in range(1, m-1):
            heapq.heappush(heap, [heightMap[i][0], i, 0])
            visited[i][0] = True
            heapq.heappush(heap, [heightMap[i][n-1], i, n-1])
            visited[i][n-1] = True
        # loop
        while heap:
            hh, xx, yy = heapq.heappop(heap)
            for dx, dy in direct:
                x, y = xx + dx, yy + dy
                if 0 <= x < m and 0 <= y < n and not visited[x][y]:
                    visited[x][y] = True
                    h = heightMap[x][y]
                    if h < hh:
                        res += hh - h
                        h = hh
                    heapq.heappush(heap, [h, x, y])
        return res


heightMap = [[3, 3, 3, 3, 3], [3, 2, 2, 2, 3], [
    3, 2, 1, 2, 3], [3, 2, 2, 2, 3], [3, 3, 3, 3, 3]]
obj = Solution()
print(obj.trapRainWater(heightMap))
