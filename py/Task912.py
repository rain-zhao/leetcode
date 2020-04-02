# 给你一个整数数组 nums，将该数组升序排列。

#  

# 示例 1：

# 输入：nums = [5,2,3,1]
# 输出：[1,2,3,5]
# 示例 2：

# 输入：nums = [5,1,1,2,0,0]
# 输出：[0,0,1,1,2,5]

from typing import List
import random


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return sorted(nums)

    # quick sort
    def sortArray2(self, nums: List[int]) -> List[int]:
        def quickSort(start: int, end: int):
            # terminator
            if start >= end:
                return

            # rand pos and swap into first
            pos = random.randint(start, end)
            nums[pos], nums[start] = nums[start], nums[pos]

            left, right = start + 1, end

            # split the array
            while left <= right:
                if nums[start] >= nums[left]:
                    left += 1
                else:
                    nums[left], nums[right] = nums[right], nums[left]
                    right -= 1

            # swap pos into middle
            nums[start], nums[right] = nums[right], nums[start]

            # sort sub-array
            quickSort(start, right-1)
            quickSort(left, end)

        quickSort(0, len(nums)-1)
        return nums


obj = Solution()
nums = [5, 1, 1, 2, 0, 0]
print(obj.sortArray2(nums))
