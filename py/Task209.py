from typing import List


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums or sum(nums) < s:
            return 0
        left = right = 0
        l = len(nums)
        cursum = 0
        mini = l
        while True:
            if cursum < s:
                if right == l:
                    break
                cursum += nums[right]
                right += 1
            else:
                mini = min(mini, right-left)
                cursum -= nums[left]
                left += 1
        return mini

    def minSubArrayLen2(self, s: int, nums: List[int]) -> int:
        if not nums or sum(nums) < s:
            return 0
        l = len(nums)
        cursum = 0
        mini = l
        left = 0
        for right in range(l):
            cursum += nums[right]
            while cursum >= s:
                mini = min(mini, right-left+1)
                cursum -= nums[left]
                left += 1
        return mini


s = 213
nums = [12, 28, 83, 4, 25, 26, 25, 2, 25, 25, 25, 12]
so = Solution()
print(so.minSubArrayLen(s, nums))
