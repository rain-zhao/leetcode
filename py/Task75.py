from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)
        left, right, p = 0, n-1, 0
        while p <= right:
            if nums[p] == 2:
                nums[p], nums[right] = nums[right], nums[p]
                right -= 1
            elif nums[p] == 0:
                nums[p], nums[left] = nums[left], nums[p]
                left += 1
                p += 1
            else:
                p += 1


nums = [2, 0, 2, 1, 1, 0]
obj = Solution()
print(obj.sortColors(nums))
