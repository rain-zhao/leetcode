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

    def connected(self, x, y) -> bool:
        return self.findRoot(x) == self.findRoot(y)


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        uf1, uf2 = UnionFind(n+1), UnionFind(n+1)
        res = 0
        edges.sort(reverse=True)
        for type, u, v in edges:
            if type == 3:
                if uf1.connected(u, v) and uf2.connected(u, v):
                    res += 1
                else:
                    uf1.union(u, v)
                    uf2.union(u, v)
            elif type == 1:
                if uf1.connected(u, v):
                    res += 1
                else:
                    uf1.union(u, v)
            else:
                if uf2.connected(u, v):
                    res += 1
                else:
                    uf2.union(u, v)

        # check if all connected
        if len(set([uf1.findRoot(i) for i in range(1, n)])) == 1 and \
                len(set([uf2.findRoot(i) for i in range(1, n)])) == 1:
            return res
        else:
            return -1


n = 4
edges = [[3,1,2],[3,2,3],[1,1,4],[2,1,4]]
obj = Solution()
print(obj.maxNumEdgesToRemove(n,edges))