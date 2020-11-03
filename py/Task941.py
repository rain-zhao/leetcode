from typing import List


class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        l = len(A)
        if l < 3:
            return False
        i = 0
        while i < l-1 and A[i] < A[i+1]:
            i += 1
        if i == 0 or i == l-1:
            return False
        while i < l-1 and A[i] > A[i+1]:
            i += 1
        return i == l-1


A = [0,3,2,1]
obj = Solution()
print(obj.validMountainArray(A))
