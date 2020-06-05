# 输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。

#  

# 示例 1：

# 输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
# 输出：[1,2,3,6,9,8,7,4,5]
# 示例 2：

# 输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# 输出：[1,2,3,4,8,12,11,10,9,5,6,7]

from typing import List


class Solution:
    # visit记录是否已经访问过
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        direct = ((0, 1), (1, 0), (0, -1), (-1, 0))
        res = []
        lx, ly = len(matrix), len(matrix[0])
        visit = [[0] * ly for _ in range(lx)]
        px, py = (0, -1)
        while len(res) < lx * ly:
            for dx, dy in direct:
                while 1:
                    x, y = px + dx, py + dy
                    if 0 <= x < lx and 0 <= y < ly and not visit[x][y]:
                        res.append(matrix[x][y])
                        visit[x][y] = 1
                        px, py = x, y
                    else:
                        break
        return res

    # 记录上，下，左，右标
    def spiralOrder2(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        res = []
        lx, ly = len(matrix), len(matrix[0])
        top, bottom, left, right = 0, lx-1, 0, ly-1
        while 1:
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            top += 1
            if len(res) == lx * ly:
                break
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1
            if len(res) == lx * ly:
                break
            for i in range(right, left - 1, -1):
                res.append(matrix[bottom][i])
            bottom -= 1
            if len(res) == lx * ly:
                break
            for i in range(bottom, top - 1, -1):
                res.append(matrix[i][left])
            left += 1
            if len(res) == lx * ly:
                break
        return res


obj = Solution()
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# matrix = [[1], [2], [3], [4]]
print(obj.spiralOrder2(matrix))
