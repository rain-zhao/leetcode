from typing import Counter, List


class Solution:
    # using heap
    def distributeCandies(self, candyType: List[int]) -> int:
        return min(len(set(candyType)), len(candyType) >> 1)


candies = [1, 1, 2, 2, 3, 3]
obj = Solution()
print(obj.distributeCandies(candies))
