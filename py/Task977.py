from typing import List


class Solution:
    # sort
    def sortedSquares(self, A: List[int]) -> List[int]:
        return sorted(map(lambda x: x**2, A))

    # double cursor
    def sortedSquares2(self, A: List[int]) -> List[int]:
        # find first num get 0 using binary search
        left, right = 0, len(A)-1
        while left <= right:
            mid = (left + right) >> 1
            if A[mid] < 0:
                left = mid + 1
            else:
                right = mid - 1
        p1, p2 = right, left
        res = []
        while p1 >= 0 and p2 < len(A):
            if -A[p1] < A[p2]:
                res.append(A[p1]**2)
                p1 -= 1
            else:
                res.append(A[p2]**2)
                p2 += 1
        while p1 >= 0:
            res.append(A[p1]**2)
            p1 -= 1
        while p2 < len(A):
            res.append(A[p2]**2)
            p2 += 1
        return res

    # double cursor optimize code
    def sortedSquares3(self, A: List[int]) -> List[int]:
        left, right = 0, len(A)-1
        res = []
        while left < right:
            if A[left]**2 > A[right]**2:
                res.append(A[left]**2)
                left += 1
            else:
                res.append(A[right]**2)
                right -= 1
        res.append(A[left]**2)
        return reversed(res)


A = [-4, -1, 0, 3, 10]
obj = Solution()
print(obj.sortedSquares3(A))
