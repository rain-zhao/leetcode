# 地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。一个机器人从坐标 [0, 0] 的格子开始移动，它每次可以向左、右、上、下移动一格（不能移动到方格外），也不能进入行坐标和列坐标的数位之和大于k的格子。例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。但它不能进入方格 [35, 38]，因为3+5+3+8=19。请问该机器人能够到达多少个格子？

#  

# 示例 1：

# 输入：m = 2, n = 3, k = 1
# 输出：3
# 示例 1：

# 输入：m = 3, n = 1, k = 0
# 输出：1
# 提示：

# 1 <= n,m <= 100
# 0 <= k <= 20
from collections import deque


class Solution:
    # dfs
    def movingCount(self, m: int, n: int, k: int) -> int:
        def check(x: int, y: int) -> bool:
            cnt = 0
            while x:
                x, cnt = x // 10, cnt + x % 10
            while y:
                y, cnt = y // 10, cnt + y % 10
            return cnt <= k
        visit = {0}
        self.res = 1
        # direct = ((0, 1), (0, -1), (1, 0), (-1, 0))
        # 方向数组只需要向下和向右
        direct = ((0, 1), (1, 0))

        def dfs(x: int, y: int):
            for dx, dy in direct:
                i, j = x + dx, y + dy
                if 0 <= i < m and 0 <= j < n and n * i + j not in visit and check(i, j):
                    visit.add(n * i + j)
                    self.res += 1
                    dfs(i, j)
        dfs(0, 0)
        return self.res

    # bfs
    def movingCount2(self, m: int, n: int, k: int) -> int:
        def check(x: int, y: int) -> bool:
            cnt = 0
            while x:
                x, cnt = x // 10, cnt + x % 10
            while y:
                y, cnt = y // 10, cnt + y % 10
            return cnt <= k

        # 方向数组只需要向下和向右
        direct = ((0, 1), (1, 0))

        visit = {0}
        dq = deque()
        dq.append((0, 0))
        res = 1
        while dq:
            x, y = dq.popleft()
            for dx, dy in direct:
                i, j = x + dx, y + dy
                if 0 <= i < m and 0 <= j < n and n * i + j not in visit and check(i, j):
                    visit.add(n * i + j)
                    res += 1
                    dq.append((i, j))

        return res


m = 2
n = 3
k = 1
obj = Solution()
print(obj.movingCount2(m, n, k))
