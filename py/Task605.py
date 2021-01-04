from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # 对于开头连续的0区间，左边没有0限制，可以认为最左边有一个0
        k = 1
        for i in flowerbed:
            if i == 0:
                k += 1
            else:
                n -= (k-1) >> 1
                k = 0
        # 结尾的连续0区间，右边没有0限制，不用-1
        n -= k >> 1
        return n <= 0


flowerbed = [1, 0, 0, 0, 1]
n = 1
obj = Solution()
print(obj.canPlaceFlowers(flowerbed, n))
