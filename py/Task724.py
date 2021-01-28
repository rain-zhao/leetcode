from typing import List


class Solution:
    # left & right
    def pivotIndex(self, nums: List[int]) -> int:
        left, right = 0, sum(nums)
        for idx, num in enumerate(nums):
            right -= num
            if left == right:
                return idx
            left += num
        return -1


nums = [1, 7, 3, 6, 5, 6]
obj = Solution()
print(obj.pivotIndex(nums))
