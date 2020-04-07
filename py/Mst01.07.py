# 给你一幅由 N × N 矩阵表示的图像，其中每个像素的大小为 4 字节。请你设计一种算法，将图像旋转 90 度。

# 不占用额外内存空间能否做到？

#  

# 示例 1:

# 给定 matrix =
# [
#   [1,2,3],
#   [4,5,6],
#   [7,8,9]
# ],

# 原地旋转输入矩阵，使其变为:
# [
#   [7,4,1],
#   [8,5,2],
#   [9,6,3]
# ]
# 示例 2:

# 给定 matrix =
# [
#   [ 5, 1, 9,11],
#   [ 2, 4, 8,10],
#   [13, 3, 6, 7],
#   [15,14,12,16]
# ],

# 原地旋转输入矩阵，使其变为:
# [
#   [15,13, 2, 5],
#   [14, 3, 4, 1],
#   [12, 6, 8, 9],
#   [16, 7,10,11]
# ]

from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        N = len(matrix)
        if not N:
            return

        for i in range((N+1) >> 1):
            for j in range(i, N-i-1):
                x, y, tmp = i, j, matrix[i][j]
                for _ in range(4):
                    matrix[y][N-1-x], tmp, x, y = tmp, matrix[y][N-1-x], y, N-1-x

    def rotate2(self, matrix: List[List[int]]) -> None:
        N = len(matrix)
        if not N:
            return
        for i in range((N+1) >> 1):
            for j in range(i, N-i-1):
                x, y = i, j
                for _ in range(3):
                    matrix[x][y], matrix[N-1-y][x], x, y = \
                        matrix[N-1-y][x], matrix[x][y], N-1-y, x


obj = Solution()
matrix = [
    [5, 1, 9, 11],
    [2, 4, 8, 10],
    [13, 3, 6, 7],
    [15, 14, 12, 16]
]
obj.rotate2(matrix)
print(matrix)
