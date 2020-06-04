# 给你一个长度为 n 的整数数组 nums，其中 n > 1，返回输出数组 output ，其中 output[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积。

#  

# 示例:

# 输入: [1,2,3,4]
# 输出: [24,12,8,6]
#  

# 提示：题目数据保证数组之中任意元素的全部前缀元素和后缀（甚至是整个数组）的乘积都在 32 位整数范围内。

# 说明: 请不要使用除法，且在 O(n) 时间复杂度内完成此题。

# 进阶：
# 你可以在常数空间复杂度内完成这个题目吗？（ 出于对空间复杂度分析的目的，输出数组不被视为额外空间。）
from typing import List


class Solution:
    # 左边乘一遍右边乘一遍
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        left = [1] * l
        right = [1] * l

        for i in range(l - 1):
            left[i + 1] = left[i] * nums[i]

        for i in range(l - 1, 0, -1):
            right[i - 1] = right[i] * nums[i]

        res = []
        for a, b in zip(left, right):
            res.append(a * b)

        return res

    # 原地操作
    def productExceptSelf2(self, nums: List[int]) -> List[int]:
        l = len(nums)
        res = [1] * l

        # left to right
        cur = 1
        for i in range(l - 1):
            cur *= nums[i]
            res[i + 1] = cur

        # right to left
        cur = 1
        for i in range(l - 1, 0, -1):
            cur *= nums[i]
            res[i - 1] *= cur

        return res


nums = [1, 2, 3, 4]
obj = Solution()
print(obj.productExceptSelf2(nums))
