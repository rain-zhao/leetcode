from typing import List
from typing import Tuple
from queue import Queue


class Solution:

    def minimalSteps(self, maze: List[str]) -> int:
        m, n = len(maze), len(maze[0])
        direct = ((0, 1), (0, -1), (1, 0), (-1, 0))

        # define bfs 函数计算点到所有点的最短距离,-1代表不可达
        # input: (i,j) 起点坐标
        # return: 到所有点的最短距离
        def bfs(i: int, j: int) -> List[List[int]]:
            res = [[-1] * n for _ in range(m)]
            res[i][j] = 0
            q = Queue()
            q.put((i, j))
            while not q.empty():
                x, y = q.get()
                for dx, dy in direct:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m \
                            and 0 <= ny < n \
                            and maze[nx][ny] != '#' \
                            and res[nx][ny] == -1:
                        res[nx][ny] = res[x][y] + 1
                        q.put((nx, ny))
            return res

        buttons = []
        stones = []
        # 起点 & 终点
        sx = sy = tx = ty = -1

        # 找出所有 起点/终点/机关/石头
        for i in range(m):
            for j in range(n):
                c = maze[i][j]
                if c == 'S':
                    sx, sy = i, j
                elif c == 'T':
                    tx, ty = i, j
                elif c == 'O':
                    stones.append((i, j))
                elif c == 'M':
                    buttons.append((i, j))

        nb = len(buttons)
        ns = len(stones)

        # 起点到所有点的距离
        # 用于计算起点到所有bottuns的距离
        startDist = bfs(sx, sy)

        # 极端情况：没有机关，字节计算起点到终点的距离
        if nb == 0:
            return startDist[tx][ty]

        # 某个机关到其他机关/起点/终点的最短距离
        dist = [[-1] * (nb + 2) for _ in range(nb)]

        # 中间结果
        dd = []
        for i in range(nb):
            bx, by = buttons[i]
            d = bfs(bx, by)
            dd.append(d)
            # buton到终点不需要拿石头
            dist[i][-1] = d[tx][ty]

        # 计算机关到机关的距离
        for i in range(nb):
            d = dd[i]
            # 计算机关到起点的距离
            for k in range(ns):
                midX, midY = stones[k]
                if startDist[midX][midY] != -1 and d[midX][midY] != -1:
                    if dist[i][-2] == -1:
                        dist[i][-2] = startDist[midX][midY] + d[midX][midY]
                    else:
                        dist[i][-2] = min(dist[i][-2],
                                          startDist[midX][midY] + d[midX][midY])

            # 计算机关到机关的距离
            for j in range(i+1, nb):
                dj = dd[j]
                mn = -1
                for k in range(ns):
                    midX, midY = stones[k]
                    if d[midX][midY] != -1 and dj[midX][midY] != -1:
                        if mn == -1:
                            mn = d[midX][midY] + dj[midX][midY]
                        else:
                            mn = min(mn,
                                     d[midX][midY] + dj[midX][midY])
                dist[i][j] = mn
                dist[j][i] = mn

        # 无法达成的情况
        for i in range(nb):
            if dist[i][-1] == -1 or dist[i][-2] == -1:
                return -1

        #  define dp array
        # dp[i][j] = 当前在第j个机关 mask 为i的最小步数
        dp = [[-1] * nb for _ in range(1 << nb)]
        # init
        for i in range(nb):
            dp[1 << i][i] = dist[i][-2]

        for mask in range(1, 1 << nb):
            for i in range(nb):
                # 有效的dp
                if mask & (1 << i) == 0:
                    continue
                # 增加多一位
                for j in range(nb):
                    if mask & (1 << j) != 0:
                        continue
                    next = mask | (1 << j)
                    if dp[next][j] == -1:
                        dp[next][j] = dp[mask][i] + dist[i][j]
                    else:
                        dp[next][j] = min(
                            dp[next][j], dp[mask][i] + dist[i][j])

        # 计算结果
        finalMask = (1 << nb) - 1
        res = -1
        for i in range(nb):
            if res == -1:
                res = dp[finalMask][i] + dist[i][-1]
            else:
                res = min(res, dp[finalMask][i] + dist[i][-1])
        return res


maze = ["S#O", "M..", "M.T"]
obj = Solution()
print(obj.minimalSteps(maze))
