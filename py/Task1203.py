from typing import List
from collections import defaultdict
from queue import Queue


class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        # def topoSort(adjList: List[List[int]], inDegreeList: List[int]) -> List[int]:
        #     n = len(adjList)
        #     res = []
        #     q = Queue()
        #     for i in range(n):
        #         if not inDegreeList[i]:
        #             q.put(i)
        #     while not q.empty():
        #         item = q.get()
        #         res.append(item)
        #         for successor in adjList[item]:
        #             inDegreeList[successor] -= 1
        #             if inDegreeList[successor] == 0:
        #                 q.put(successor)
        #     return res if len(res) == n else None

        # 改成用stack
        def topoSort(adjList: List[List[int]], inDegreeList: List[int]) -> List[int]:
            n = len(adjList)
            res = []
            q = []
            for i in range(n):
                if not inDegreeList[i]:
                    q.append(i)
            while q:
                item = q.pop()
                res.append(item)
                for successor in adjList[item]:
                    inDegreeList[successor] -= 1
                    if inDegreeList[successor] == 0:
                        q.append(successor)
            return res if len(res) == n else None

        # 处理未分组
        for i in range(n):
            if group[i] == -1:
                group[i] = m
                m += 1
        # 生成邻接矩阵和统计入度
        adjGroup = [[] for _ in range(m)]
        adjItem = [[] for _ in range(n)]
        inDegreeGroup = [0] * m
        inDegreeItem = [0] * n

        for i in range(n):
            curGroup = group[i]
            for beforeItem in beforeItems[i]:
                beforeGroup = group[beforeItem]
                # item统计
                inDegreeItem[i] += 1
                adjItem[beforeItem].append(i)
                # group统计
                if curGroup != beforeGroup:
                    inDegreeGroup[curGroup] += 1
                    adjGroup[beforeGroup].append(curGroup)

        # 对group 和item进行拓扑排序
        groupOrdList = topoSort(adjGroup, inDegreeGroup)
        if not groupOrdList:
            return []
        itemOrdList = topoSort(adjItem, inDegreeItem)
        if not itemOrdList:
            return []

        # item和group的依赖
        groupItemOrdList = [[] for _ in range(m)]
        for i in itemOrdList:
            groupItemOrdList[group[i]].append(i)
        # 返回结果
        res = []
        for g in groupOrdList:
            res += groupItemOrdList[g]

        return res


obj = Solution()
n = 8
m = 2
group = [-1, -1, 1, 0, 0, 1, 0, -1]
beforeItems = [[], [6], [5], [6], [3, 6], [], [], []]
print(obj.sortItems(n, m, group, beforeItems))
