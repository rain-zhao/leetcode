from typing import List
from collections import deque


class Solution:
    # deque
    def longestOnes(self, A: List[int], K: int) -> int:
        res = 0
        dq = deque([-1], K+1)
        for idx, i in enumerate(A):
            if i == 0:
                dq.append(idx)
            res = max(res, idx - dq[0])
        return res

    # slide window
    def longestOnes2(self, A: List[int], K: int) -> int:
        left = count = 0
        res = 0
        for idx, i in enumerate(A):
            if i == 0:
                count += 1
                if count > K:
                    while A[left] == 1:
                        left += 1
                    count -= 1
                    left += 1
            res = max(res, idx - left + 1)
        return res


A = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]
K = 3
obj = Solution()
print(obj.longestOnes2(A, K))
