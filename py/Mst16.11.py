from typing import List


class Solution:
    def divingBoard(self, shorter: int, longer: int, k: int) -> List[int]:
        if k == 0:
            return []
        length = shorter * k
        delta = longer - shorter
        if delta == 0:
            return [length, ]
        res = []
        for _ in range(k+1):
            res.append(length)
            length += delta
        return res


shorter = 1
longer = 2
k = 0
obj = Solution()
print(obj.divingBoard(shorter, longer, k))
