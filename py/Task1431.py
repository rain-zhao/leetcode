
from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxVal = max(candies)
        res = [candy + extraCandies >= maxVal for candy in candies]
        return res
