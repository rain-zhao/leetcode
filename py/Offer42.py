from typing import List


class Solution:
    # dp
    def maxSubArray(self, nums: List[int]) -> int:
        dp = nums[:]
        for i in range(1, len(nums)):
            if dp[i-1] > 0:
                dp[i] += dp[i-1]
        return max(dp)

    # dp + compression
    def maxSubArray2(self, nums: List[int]) -> int:
        res = cur = nums[0]
        for num in nums[1:]:
            cur = cur + num if cur > 0 else num
            res = max(res, cur)
        return res


obj = Solution()
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(obj.maxSubArray2(nums))
