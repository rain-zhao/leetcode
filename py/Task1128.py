from typing import List
from collections import defaultdict


class Solution:
    # hash
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        counts = defaultdict(int)
        for dominoe in dominoes:
            counts[str(sorted(dominoe))] += 1
        res = 0
        for count in counts.values():
            res += count * (count-1) >> 1
        return res


dominoes = [[1, 2], [2, 1], [3, 4], [5, 6], [1, 2]]
obj = Solution()
print(obj.numEquivDominoPairs(dominoes))
