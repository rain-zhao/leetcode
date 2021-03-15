from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        direct = ((0, 1), (1, 0), (0, -1), (-1, 0))
        visited = [[0] * n for _ in range(m)]
        res = []
        # begin position
        x, y = 0, -1
        while len(res) < m * n:
            for dx, dy in direct:
                xx, yy = x + dx, y + dy
                while 0 <= xx < m and 0 <= yy < n and not visited[xx][yy]:
                    x, y = xx, yy
                    visited[x][y] = 1
                    res.append(matrix[x][y])
                    xx, yy = x + dx, y + dy
        return res


matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
obj = Solution()
print(obj.spiralOrder(matrix))
