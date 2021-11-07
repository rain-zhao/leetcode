from typing import List


class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        x, y = m, n
        for xx, yy in ops:
            x, y = min(x, xx), min(y, yy)
        return x * y


obj = Solution()
m = 3
n = 3
operations = [[2, 2], [3, 3]]
print(obj.maxCount(m, n, operations))
