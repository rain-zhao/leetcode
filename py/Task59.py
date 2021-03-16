from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0] * n for _ in range(n)]
        direct = ((0, 1), (1, 0), (0, -1), (-1, 0))
        i = 1
        x, y = 0, -1
        while i <= n ** 2:
            for dx, dy in direct:
                xx, yy = x + dx, y + dy
                while 0 <= xx < n and 0 <= yy < n and res[xx][yy] == 0:
                    x, y = xx, yy
                    res[x][y] = i
                    i += 1
                    xx, yy = x + dx, y + dy
        return res


n = 3
obj = Solution()
print(obj.generateMatrix(n))
