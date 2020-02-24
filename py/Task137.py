from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones = twos = 0
        for i in nums:
            ones = ones ^ i & twos
            twos = twos ^ i & ones
        return ones


so = Solution()
nums = [0, 1, 0, 1, 0, 1, 99]
print(so.singleNumber(nums))
