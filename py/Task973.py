from typing import List
import heapq


class Solution:
    # priority queue
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        if len(points) <= K:
            return points
        pq = []
        for point in points:
            score = - point[0] ** 2 - point[1] ** 2
            if len(pq) < K:
                heapq.heappush(pq, (score, point))
            elif pq[0][0] < score:
                heapq.heapreplace(pq, (score, point))
        return [itm[1] for itm in pq]

    # quick select
    def kClosest2(self, points: List[List[int]], K: int) -> List[List[int]]:
        if len(points) <= K:
            return points
        def score(i):
            return points[i][0] ** 2 + points[i][1] ** 2

        def quickSelect(beg: int, end: int) -> int:
            pivot = beg
            for i in range(beg, end):
                if score(i) < score(end):
                    points[i], points[pivot] = points[pivot], points[i]
                    pivot += 1
            points[pivot], points[end] = points[end], points[pivot]
            return pivot

        beg, end = 0, len(points) - 1
        while True:
            pivot = quickSelect(beg, end)
            if pivot == K:
                return points[:pivot]
            elif pivot < K:
                beg = pivot + 1
            else:
                end = pivot - 1
        return None


points = [[0,1],[1,0]]
K = 2
obj = Solution()
print(obj.kClosest2(points, K))
