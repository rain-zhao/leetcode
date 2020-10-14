from typing import List

from collections import Counter
from functools import reduce


class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        intersect = Counter(A[0])
        for word in A[1:]:
            intersect &= Counter(word)
        return intersect.elements()

    # optimize code
    def commonChars2(self, A: List[str]) -> List[str]:
        return list(reduce(lambda x, y: x & y, map(Counter, A)).elements())


A = ["bella", "label", "roller"]
obj = Solution()
print(obj.commonChars2(A))
