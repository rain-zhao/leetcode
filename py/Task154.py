# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。

# ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

# 请找出其中最小的元素。

# 注意数组中可能存在重复的元素。

# 示例 1：

# 输入: [1,3,5]
# 输出: 1
# 示例 2：

# 输入: [2,2,2,0,1]
# 输出: 0
# 说明：

# 这道题是 寻找旋转排序数组中的最小值 的延伸题目。
# 允许重复会影响算法的时间复杂度吗？会如何影响，为什么？

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        # remove redundance
        tmp = [nums[0]]
        visited = {nums[0]}
        for num in nums[1:]:
            if num not in visited:
                tmp.append(num)
                visited.add(num)
        nums = tmp

        # do as pre task
        if len(nums) == 1 or nums[0] < nums[-1]:
            return nums[0]
        left, right = 1, len(nums)-1
        while left <= right:
            mid = (left+right)//2
            if nums[mid] < nums[mid-1]:
                return nums[mid]
            if nums[mid] >= nums[0]:
                left = mid + 1
            else:
                right = mid - 1
        return -1


