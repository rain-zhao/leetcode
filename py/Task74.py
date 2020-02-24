class Solution:
    def searchMatrix(self, matrix: [[int]], target: int) -> bool:
        list = [itm for row in matrix for itm in row]
        left, right = 0, len(list)-1

        while left <= right:
            mid = left + (right - left) // 2
            val = list[mid]
            if(val == target):
                return True
            elif val > target:
                right = mid - 1
            else:
                left = mid + 1
        return False

    def searchMatrix2(self, matrix: [[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False

        m, n = len(matrix), len(matrix[0])

        left, right = 0, m*n-1

        while left <= right:
            mid = left + (right - left) // 2
            val = matrix[mid // n][mid % n]
            if(val == target):
                return True
            elif val > target:
                right = mid - 1
            else:
                left = mid + 1
        return False


matrix = [
    [1,   3,  5,  7],
    [10, 11, 16, 20],
    [23, 30, 34, 50]
]
solution = Solution()
print(solution.searchMatrix2(matrix, 3))
