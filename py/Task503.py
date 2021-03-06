from typing import List


class Solution:
    # 单调栈
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1] * n
        stack = []
        for idx in range(n):
            while stack and nums[stack[-1]] < nums[idx]:
                preIdx = stack.pop()
                res[preIdx] = nums[idx]
            stack.append(idx)

        for idx in range(n):
            while stack and nums[stack[-1]] < nums[idx]:
                preIdx = stack.pop()
                res[preIdx] = nums[idx]
        return res
