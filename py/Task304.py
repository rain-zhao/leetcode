from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            self.sums = []
            return
        m, n = len(matrix), len(matrix[0])
        sums = [[0] * (n+1) for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                sums[i+1][j+1] = sums[i+1][j] + matrix[i][j]
        for i in range(m):
            for j in range(n):
                sums[i+1][j+1] += sums[i][j+1]
        self.sums = sums

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sums = self.sums
        return sums[row2+1][col2+1] + sums[row1][col1] -\
            sums[row1][col2+1] - sums[row2+1][col1]


# Your NumMatrix object will be instantiated and called as such:
matrix = [
    [3, 0, 1, 4, 2],
    [5, 6, 3, 2, 1],
    [1, 2, 0, 1, 5],
    [4, 1, 0, 1, 7],
    [1, 0, 3, 0, 5]
]
row1, col1, row2, col2 = 2, 1, 4, 3

obj = NumMatrix(matrix)
print(obj.sumRegion(row1, col1, row2, col2))
