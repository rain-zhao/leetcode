# 在 N * N 的网格上，我们放置一些 1 * 1 * 1  的立方体。

# 每个值 v = grid[i][j] 表示 v 个正方体叠放在对应单元格 (i, j) 上。

# 请你返回最终形体的表面积。

#  

# 示例 1：

# 输入：[[2]]
# 输出：10
# 示例 2：

# 输入：[[1,2],[3,4]]
# 输出：34
# 示例 3：

# 输入：[[1,0],[0,2]]
# 输出：16
# 示例 4：

# 输入：[[1,1,1],[1,0,1],[1,1,1]]
# 输出：32
# 示例 5：

# 输入：[[2,2,2],[2,1,2],[2,2,2]]
# 输出：46
#  

# 提示：

# 1 <= N <= 50
# 0 <= grid[i][j] <= 50
from typing import List


class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        N = len(grid)

        def _compare(source: int, x2: int, y2: int) -> int:
            target = grid[x2][y2] if 0 <= x2 < N and 0 <= y2 < N else 0
            return max(source-target, 0)

        direct = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        res = 0
        for i in range(N):
            for j in range(N):
                source = grid[i][j]
                if not source:
                    continue
                for x, y in direct:
                    res += _compare(source, i + x, j + y)
                res += 2

        return res


obj = Solution()
grid = [[1, 0], [0, 2]]
print(obj.surfaceArea(grid))
