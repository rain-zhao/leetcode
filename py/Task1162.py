from typing import List
from collections import deque


class Solution:
    # bfs
    def maxDistance(self, grid: List[List[int]]) -> int:
        N = len(grid)
        direct = ((0, 1), (0, -1), (1, 0), (-1, 0))

        def nearestLand(x: int, y: int) -> int:
            near = 0
            visit = {N*x+y}
            dq = deque()
            dq.append((x, y))
            while dq:
                near += 1
                for _ in range(len(dq)):
                    p, q = dq.popleft()
                    for dx, dy in direct:
                        i, j = p + dx, q + dy
                        if 0 <= i < N and 0 <= j < N:
                            if N*i+j in visit:
                                continue
                            if grid[i][j] == 1:
                                return near
                            dq.append((i, j))
                            visit.add(N*i+j)
            return -1

        res = -1
        for i in range(N):
            for j in range(N):
                if grid[i][j] == 0:
                    res = max(res, nearestLand(i, j))
        return res

    # dijaksla
    def maxDistance2(self, grid: List[List[int]]) -> int:
        N = len(grid)
        direct = ((0, 1), (0, -1), (1, 0), (-1, 0))

        map = [[99999999999] * N for _ in range(N)]

        dq = deque()

        for i in range(N):
            for j in range(N):
                if grid[i][j]:
                    map[i][j] = 0
                    dq.append((i, j))
        res = -1
        while dq:
            p, q = dq.popleft()
            for dx, dy in direct:
                i, j = p + dx, q + dy
                if 0 <= i < N and 0 <= j < N:
                    if map[i][j] > map[p][q] + 1:
                        map[i][j] = map[p][q] + 1
                        dq.append((i, j))
                        res = max(res, map[i][j])

        return -1 if res == 0 or res == 99999999999 else res

    def maxDistance3(self, grid: List[List[int]]) -> int:
        N = len(grid)
        dq = deque()
        visit = set()
        direct = ((0, 1), (0, -1), (1, 0), (-1, 0))

        for i in range(N):
            for j in range(N):
                if grid[i][j]:
                    visit.add(N * i + j)
                    dq.append((i, j))

        if not visit or len(visit) == N * N:
            return -1

        res = 0
        while len(visit) != N * N:
            res += 1
            for _ in range(len(dq)):
                p, q = dq.popleft()
                for dx, dy in direct:
                    i, j = p + dx, q + dy
                    if 0 <= i < N and 0 <= j < N:
                        if N * i + j in visit:
                            continue
                        dq.append((i, j))
                        visit.add(N * i + j)

        return res

    def maxDistance4(self, grid: List[List[int]]) -> int:
        N = len(grid)
        dq = deque()
        visit = set()
        direct = ((0, 1), (0, -1), (1, 0), (-1, 0))

        for i in range(N):
            for j in range(N):
                if grid[i][j]:
                    visit.add(N * i + j)
                    dq.append((i, j))

        if not visit or len(visit) == N * N:
            return -1

        res = -1
        while dq:
            res += 1
            for _ in range(len(dq)):
                p, q = dq.popleft()
                for dx, dy in direct:
                    i, j = p + dx, q + dy
                    if 0 <= i < N and 0 <= j < N and N * i + j not in visit:
                        dq.append((i, j))
                        visit.add(N * i + j)

        return res


grid = [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
obj = Solution()
print(obj.maxDistance3(grid))
