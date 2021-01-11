from typing import List
from collections import defaultdict


class UnionFind:
    def __init__(self, n) -> None:
        self.parents = [i for i in range(n)]

    def findRoot(self, n: int) -> int:
        while n != self.parents[n]:
            self.parents[n] = self.parents[self.parents[n]]
            n = self.parents[n]
        return n

    def isConnected(self, x: int, y: int) -> bool:
        return self.findRoot(x) == self.findRoot(y)

    def connect(self, x: int, y: int) -> None:
        self.parents[self.findRoot(x)] = self.findRoot(y)


class Solution:
    # union-find
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        uf = UnionFind(n)
        for p, q in pairs:
            uf.connect(p, q)
        # group
        groups = defaultdict(list)
        for i in range(n):
            groups[uf.findRoot(i)].append(s[i])
        # sort group item
        for l in groups.values():
            l.sort()
        # generate result
        res = [None] * n
        for i in range(n-1, -1, -1):
            root = uf.findRoot(i)
            res[i] = groups[root].pop()
        return ''.join(res)


obj = Solution()
s = "dcab"
pairs = [[0, 3], [1, 2], [0, 2]]
print(obj.smallestStringWithSwaps(s, pairs))
