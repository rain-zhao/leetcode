
# 给你一个整数数组 nums，请你返回其中位数为 偶数 的数字的个数。
from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        cnt = 0
        for num in nums:
            while num >= 100:
                num //= 100
            if num >= 10:
                cnt += 1
        return cnt

    def findNumbers2(self, nums: List[int]) -> int:
        cnt = 0
        for num in nums:
            if not len(str(num)) & 1:
                cnt += 1
        return cnt


so = Solution()
nums = [12, 345, 2, 6, 7896]
print(so.findNumbers2(nums))
