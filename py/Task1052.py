from typing import List


class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        res = sum([i for i, j in zip(customers, grumpy) if not j])
        maxDelta = delta = sum(
            [i for i, j in zip(customers[0:X], grumpy[0:X]) if j])
        for i in range(X, len(customers)):
            if grumpy[i] == 1:
                delta += customers[i]
            if grumpy[i-X] == 1:
                delta -= customers[i-X]
            maxDelta = max(maxDelta, delta)
        return res + maxDelta


customers = [1, 0, 1, 2, 1, 1, 7, 5]
grumpy = [0, 1, 0, 1, 0, 1, 0, 1]
X = 3
so = Solution()
print(so.maxSatisfied(customers, grumpy, X))
