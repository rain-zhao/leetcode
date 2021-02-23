from typing import List


class Solution:
    # slide window
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        origin = sum(i for i, j in zip(customers, grumpy) if not j)
        delta = sum(i for i, j in zip(customers[:X], grumpy[:X]) if j)
        res = cur = origin + delta
        for i in range(X, len(customers)):
            cur += customers[i] *  grumpy[i] - customers[i-X] * grumpy[i-X]
            res = max(res, cur)
        return res


customers = [1, 0, 1, 2, 1, 1, 7, 5]
grumpy = [0, 1, 0, 1, 0, 1, 0, 1]
X = 3
so = Solution()
print(so.maxSatisfied(customers, grumpy, X))
