from typing import List


class Solution:
    # dp
    def canPartition(self, nums: List[int]) -> bool:
        n, total, maxNum = len(nums), sum(nums), max(nums)
        if n < 2 or total & 1:
            return False
        target = total >> 1
        if maxNum > target:
            return False
        dp = [[True] + [False] * target for _ in range(n)]
        dp[0][nums[0]] = True
        for i in range(1, n):
            num = nums[i]
            for j in range(1, target+1):
                dp[i][j] = dp[i-1][j]
                if j - num >= 0:
                    dp[i][j] |= dp[i-1][j-num]
        return dp[n-1][target]

    # dp & compress
    def canPartition2(self, nums: List[int]) -> bool:
        n, total, maxNum = len(nums), sum(nums), max(nums)
        if n < 2 or total & 1:
            return False
        target = total >> 1
        if maxNum > target:
            return False
        dp = [True] + [False] * target
        for num in nums:
            for j in range(target, num-1, -1):
                dp[j] |= dp[j-num]
        return dp[target]


obj = Solution()
nums = [1, 5, 11, 5]
print(obj.canPartition2(nums))
