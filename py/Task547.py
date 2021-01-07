from typing import List


class UnionFind:
    def __init__(self, n: int) -> None:
        self.parents = [i for i in range(n)]

    def root(self, n: int) -> int:
        # find root
        k = n
        while self.parents[k] != k:
            k = self.parents[k]
        # flatten
        while self.parents[n] != n:
            self.parents[n], n = k, self.parents[n]
        return k

    def connected(self, x: int, y: int) -> bool:
        return self.root(x) == self.root(y)

    def union(self, x: int, y: int) -> None:
        self.parents[self.root(x)] = self.root(y)


class Solution:
    # find-union
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        unionFind = UnionFind(n)
        for i in range(n):
            for j in range(i+1, n):
                if isConnected[i][j]:
                    unionFind.union(i, j)
        return len(set([unionFind.root(i) for i in range(n)]))

    # dfs
    def findCircleNum2(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [0] * n
        res = 0

        def visit(i: int) -> None:
            visited[i] = 1
            for j in range(n):
                if isConnected[i][j] == 1 and not visited[j]:
                    visit(j)
        for i in range(n):
            if not visited[i]:
                res += 1
                visit(i)
        return res


obj = Solution()
isConnected = [[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 1], [1, 0, 1, 1]]
print(obj.findCircleNum2(isConnected))
