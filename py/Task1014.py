from typing import List


class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        stack = [1]
        for idx in range(2, len(A)):
            while len(stack) and A[idx] - idx >= A[stack[-1]]-stack[-1]:
                stack.pop()
            stack.append(idx)
        pos = 0
        res = 0
        for idx in range(len(A)-1):
            if idx >= stack[pos]:
                pos += 1
            res = max(res, A[idx]+idx+A[stack[pos]]-stack[pos])
        return res

    def maxScoreSightseeingPair2(self, A: List[int]) -> int:
        preMax = res = -90000000000
        for i in range(len(A)-1):
            preMax = max(preMax,A[i]+i)
            res = max(res,preMax+A[i+1]-i-1)
        return res


A = [8, 1, 5, 2, 6]
so = Solution()
print(so.maxScoreSightseeingPair2(A))
