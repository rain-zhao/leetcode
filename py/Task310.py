from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        cnts = [0]*n
        adjlist = [[] for _ in range(n)]

        for i, j in edges:
            cnts[i] += 1
            adjlist[i].append(j)
            cnts[j] += 1
            adjlist[j].append(i)

        queue = []
        for i in range(n):
            if cnts[i] == 1:
                queue.append(i)
        pos = 0
        remain = {i for i in range(n)}
        while len(remain) > 2:
            last = len(queue)
            for p in range(pos, len(queue)):
                val = queue[p]
                cnts[val] = 0
                remain.remove(val)
                for j in adjlist[val]:
                    cnts[j] -= 1
                    if cnts[j] == 1:
                        queue.append(j)
            pos = last

        return list(remain)


n = 4
edges = [[1, 0], [1, 2], [1, 3]]
so = Solution()
so.findMinHeightTrees(n, edges)
