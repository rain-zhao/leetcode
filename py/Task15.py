# 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。

# 注意：答案中不可以包含重复的三元组。

#  

# 示例：

# 给定数组 nums = [-1, 0, 1, 2, -1, -4]，

# 满足要求的三元组集合为：
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]
from typing import List


class Solution:
    # sort + hash
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []

        nums = sorted(nums)
        l = len(nums)

        res = []
        for i in range(l-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            num1 = nums[i]
            s = set()
            j = i + 1
            while j < l:
                num2 = nums[j]
                j += 1
                if num2 in s:
                    res.append([num1, num2, -num1 - num2])
                    while j < l and nums[j] == nums[j-1]:
                        j += 1
                else:
                    s.add(-num1 - num2)

        return res

    # sort + double cursor

    def threeSum2(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []

        nums = sorted(nums)
        l = len(nums)
        res = []

        for i in range(l):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            num1 = nums[i]
            left, right = i + 1, l-1
            while left < right:
                num2, num3 = nums[left], nums[right]
                if num1 + num2 + num3 == 0:
                    res.append([num1, num2, num3])
                    while left < right and nums[left] == num2:
                        left += 1
                    while left < right and nums[right] == num3:
                        right -= 1
                elif num1 + num2 + num3 < 0:
                    while left < right and nums[left] == num2:
                        left += 1
                else:
                    while left < right and nums[right] == num3:
                        right -= 1

        return res


nums = [-1, 0, 1, 2, -1, -4]
obj = Solution()
print(obj.threeSum2(nums))
