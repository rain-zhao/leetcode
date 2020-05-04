from typing import List


class Solution:
    # 1 dp
    def jump(self, nums: List[int]) -> int:
        l = len(nums)
        if l < 2:
            return 0
        dp = [999999999 for _ in range(l)]
        dp[0] = 0
        for i in range(l):
            for j in range(i+1, min(i+nums[i]+1, l)):
                dp[j] = min(dp[i] + 1, dp[j])
        return dp[-1]

    # 2 greedy
    def jump2(self, nums: List[int]) -> int:
        l = len(nums)
        if l < 2:
            return 0
        cnt = preMax = maxPos = 0
        for i, num in enumerate(nums):
            maxPos = max(maxPos, i+num)
            if maxPos >= l-1:
                return cnt+1
            if i == preMax:
                preMax = maxPos
                cnt += 1
        return cnt

    # greed 2020-05-04

    def jump3(self, nums: List[int]) -> int:
        l = len(nums)
        if l < 2:
            return 0
        res = 1
        curMax = preMax = -1
        for i, num in enumerate(nums):
            curMax = max(curMax, i + num)
            if curMax >= l - 1:
                return res
            if i >= preMax:
                res += 1
                preMax = curMax  
        return res


nums = [2, 3, 1, 1, 4]

obj = Solution()
print(obj.jump3(nums))
