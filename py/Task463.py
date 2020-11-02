from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        direct = ((1, 0), (-1, 0), (0, 1), (0, -1))
        res = 0
        m, n = len(grid), len(grid[0])
        for x in range(m):
            for y in range(n):
                if grid[x][y] == 1:
                    for dx, dy in direct:
                        xx, yy = x + dx, y + dy
                        if not 0 <= xx < m or not 0 <= yy < n or grid[xx][yy] == 0:
                            res += 1
        return res

    # dfs
    def islandPerimeter2(self, grid: List[List[int]]) -> int:
        direct = ((1, 0), (-1, 0), (0, 1), (0, -1))
        m, n = len(grid), len(grid[0])
        self.res = 0

        def dfs(x: int, y: int):
            if not 0 <= x < m or not 0 <= y < n or grid[x][y] == 0:
                self.res += 1
                return
            if grid[x][y] == 2:
                return
            grid[x][y] = 2
            for dx, dy in direct:
                dfs(x+dx, y+dy)
        for x in range(m):
            for y in range(n):
                if grid[x][y] == 1:
                    dfs(x, y)
                    return self.res
        return 0
