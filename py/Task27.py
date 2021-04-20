from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        for num in nums:
            if num != val:
                nums[i] = num
                i += 1
        return i


nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2
obj = Solution()
print(obj.removeElement(nums, val))
