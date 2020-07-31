from typing import List


class Solution:
    # brute-force
    def findMagicIndex(self, nums: List[int]) -> int:
        for i, num in enumerate(nums):
            if i == num:
                return i
        return -1

    def findMagicIndex2(self, nums: List[int]) -> int:
        p, l = 0, len(nums)
        while p < l:
            if p == nums[p]:
                return p
            elif p < nums[p]:
                p = nums[p]
            else:
                p += 1
        return -1
