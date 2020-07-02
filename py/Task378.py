# 给定一个 n x n 矩阵，其中每行和每列元素均按升序排序，找到矩阵中第 k 小的元素。
# 请注意，它是排序后的第 k 小元素，而不是第 k 个不同的元素。

#  

# 示例：

# matrix = [
#    [ 1,  5,  9],
#    [10, 11, 13],
#    [12, 13, 15]
# ],
# k = 8,

# 返回 13。
from typing import List
import heapq


class Solution:
    # merge sort
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        heap = [(row[0], row, 0) for row in matrix]
        for _ in range(k - 1):
            _, row, idx = heap[0]
            if idx + 1 < n:
                heapq.heapreplace(heap, (row[idx+1], row, idx+1))
            else:
                heapq.heappop(heap)
        return heap[0][0]

    # binary search
    def kthSmallest2(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        left, right = matrix[0][0], matrix[-1][-1]
        while left <= right:
            mid = (left + right) >> 1
            count = 0
            x, y = n-1, 0
            while 0 <= x and y < n:
                if matrix[x][y] <= mid:
                    count += x + 1
                    y += 1
                else:
                    x -= 1
            if count < k:
                left = mid + 1
            else:
                right = mid - 1
        return left


matrix = [
    [1,  5,  9],
    [10, 11, 13],
    [12, 13, 15]
]
k = 8

obj = Solution()
print(obj.kthSmallest2(matrix, k))
