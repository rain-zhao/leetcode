class Solution:
    def rob(self, nums: [int]) -> int:
        if not nums:
            return 0
        if len(nums) < 3:
            return max(nums)

        def helper(nums):
            # init
            dp = [0] * len(nums)
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])

            for i, num in enumerate(nums[2:], 2):
                dp[i] = max(dp[i-2]+num, dp[i-1])
            return dp[-1]

        return max(helper(nums[1:]), helper(nums[:-1]))
