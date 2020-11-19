from typing import List


class Solution:
    # swap
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        p = 0
        for i in range(n):
            if nums[i] != 0:
                nums[i], nums[p] = nums[p], nums[i]
                p += 1

    # 直接替换，最后赋0
    def moveZeroes2(self, nums: List[int]) -> None:
        n = len(nums)
        p = 0
        for num in nums:
            if num!= 0:
                nums[p] = num
                p += 1
        for i in range(p, n):
            nums[i] = 0

nums = [0, 1, 0, 3, 12]
obj = Solution()
print(obj.moveZeroes2(nums))
