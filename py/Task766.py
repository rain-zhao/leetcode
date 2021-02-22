from typing import List


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        row0 = matrix[0]
        for row in matrix[1:]:
            for item0, item in zip(row0, row[1:]):
                if item0 != item:
                    return False
            row0 = row
        return True


matrix = [[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]]
obj = Solution()
print(obj.isToeplitzMatrix(matrix))
