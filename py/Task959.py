from typing import List


class UnionFind:
    def __init__(self, n) -> None:
        self.parent = [i for i in range(n)]

    def union(self, x, y):
        self.parent[self.findRoot(x)] = self.findRoot(y)

    def findRoot(self, x) -> int:
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x


class Solution:
    # union-find
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        uf = UnionFind(n**2 * 4)
        for i in range(n):
            for j in range(n):
                idx = i * n + j
                # down
                if i < n-1:
                    down = idx + n
                    uf.union(idx * 4 + 2, down * 4)
                # right
                if j < n-1:
                    right = idx + 1
                    uf.union(idx * 4 + 1, right * 4 + 3)
                if grid[i][j] == '/':
                    uf.union(idx * 4, idx * 4 + 3)
                    uf.union(idx * 4 + 1, idx * 4 + 2)
                elif grid[i][j] == '\\':
                    uf.union(idx * 4, idx * 4 + 1)
                    uf.union(idx * 4 + 2, idx * 4 + 3)
                else:
                    uf.union(idx * 4, idx * 4 + 1)
                    uf.union(idx * 4, idx * 4 + 2)
                    uf.union(idx * 4, idx * 4 + 3)
        return len(set([uf.findRoot(i) for i in range(n**2 * 4)]))


obj = Solution()
grid = [
    "/\\",
    "\\/"
]
print(obj.regionsBySlashes(grid))
