# 在本问题中，有根树指满足以下条件的有向图。该树只有一个根节点，所有其他节点都是该根节点的后继。每一个节点只有一个父节点，除了根节点没有父节点。

# 输入一个有向图，该图由一个有着N个节点 (节点值不重复1, 2, ..., N) 的树及一条附加的边构成。附加的边的两个顶点包含在1到N中间，这条附加的边不属于树中已存在的边。

# 结果图是一个以边组成的二维数组。 每一个边 的元素是一对 [u, v]，用以表示有向图中连接顶点 u 和顶点 v 的边，其中 u 是 v 的一个父节点。

# 返回一条能删除的边，使得剩下的图是有N个节点的有根树。若有多个答案，返回最后出现在给定二维数组的答案。

# 示例 1:

# 输入: [[1,2], [1,3], [2,3]]
# 输出: [2,3]
# 解释: 给定的有向图如下:
#   1
#  / \
# v   v
# 2-->3
# 示例 2:

# 输入: [[1,2], [2,3], [3,4], [4,1], [1,5]]
# 输出: [4,1]
# 解释: 给定的有向图如下:
# 5 <- 1 -> 2
#      ^    |
#      |    v
#      4 <- 3
# 注意:

# 二维数组大小的在3到1000范围内。
# 二维数组中的每个整数在1到N之间，其中 N 是二维数组的大小。

from typing import List

from typing import List


class UnionFind:
    def __init__(self, size: int):
        # 从1开始数
        self.parents = [i for i in range(size+1)]

    def findRoot(self, idx: int) -> int:
        # 隔代压缩
        while idx != self.parents[idx]:
            self.parents[idx] = self.parents[self.parents[idx]]
            idx = self.parents[idx]
        return idx

    def union(self, p: int, q: int) -> None:
        self.parents[self.findRoot(p)] = self.findRoot(q)

    def connected(self, p: int, q: int) -> bool:
        return self.findRoot(p) == self.findRoot(q)


class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        uf = UnionFind(n)
        parents = [i for i in range(n+1)]
        confict = -1
        cycle = -1
        for i, (u, v) in enumerate(edges):
            # check confict
            if parents[v] != v:
                confict = i
            else:
                parents[v] = u
                # check cycle
                if uf.connected(u, v):
                    cycle = i
                else:
                    uf.union(u, v)
        # find bad edge
        if confict == -1:
            return edges[cycle]
        if cycle == -1:
            return edges[confict]
        _, v = edges[confict]
        return [parents[v], v]


edges = [[1, 2], [1, 3], [2, 3]]
obj = Solution()
print(obj.findRedundantDirectedConnection(edges))
