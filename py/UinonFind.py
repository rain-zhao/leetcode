# implement of union & find using iteration
# class UnionFind:
#     def __init__(self, size):
#         self.parents = [i for i in range(size)]

#     def findRooot(self, idx: int) -> int:
#         if idx == self.parents[idx]:
#             return idx
#         root = idx
#         # find the root
#         while root != self.parents[root]:
#             root = self.parents[root]
#         # set parents to the root
#         while self.parents[idx] != root:
#             idx, self.parents[idx] = self.parents[idx], root
#         return root

#     def union(self, p: int, q: int) -> None:
#         r1 = self.findRooot(p)
#         r2 = self.findRooot(q)
#         self.parents[r1] = r2

#     def connected(self, p: int, q: int) -> bool:
#         return self.findRooot(p) == self.findRooot(q)

# implement of union & find using recursion


class UnionFind:
    def __init__(self, size):
        self.parents = [i for i in range(size)]

    def findRooot(self, idx: int) -> int:
        if idx == self.parents[idx]:
            return idx
        self.parents[idx] = self.findRooot(self.parents[idx])
        return self.parents[idx]

    def union(self, p: int, q: int) -> None:
        r1 = self.findRooot(p)
        r2 = self.findRooot(q)
        self.parents[r1] = r2

    def connected(self, p: int, q: int) -> bool:
        return self.findRooot(p) == self.findRooot(q)
