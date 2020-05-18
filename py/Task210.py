from typing import List
from collections import defaultdict
from queue import SimpleQueue


class Solution:
    # bfs
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        cnts = [0] * numCourses
        adjList = defaultdict(list)

        for a, b in prerequisites:
            cnts[a] += 1
            adjList[b].append(a)

        q = SimpleQueue()
        res = []
        for idx, cnt in enumerate(cnts):
            if cnt == 0:
                q.put(idx)
                res.append(idx)

        while not q.empty():
            for i in adjList[q.get()]:
                cnts[i] -= 1
                if cnts[i] == 0:
                    q.put(i)
                    res.append(i)

        return res if len(res) == numCourses else []

    # dfs
    def findOrder2(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        colors = [0] * numCourses
        adjList = defaultdict(list)

        res = []

        for a, b in prerequisites:
            adjList[a].append(b)

        def dfs(i: int) -> bool:
            if colors[i] == 1:
                return False
            if colors[i] == 2:
                return True

            colors[i] = 1
            for need in adjList[i]:
                if not dfs(need):
                    return False
            colors[i] = 2
            res.append(i)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []

        return res


numCourses = 4
prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
obj = Solution()
print(obj.findOrder2(numCourses, prerequisites))
