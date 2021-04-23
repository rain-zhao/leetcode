from typing import List


class Solution:
    # dp
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[j] >= dp[i]:
                    dp[i] = dp[j] + 1

        # find maxVal and maxLen
        maxVal = maxLen = maxIdx = 0
        for i, size in enumerate(dp):
            if size > maxLen:
                maxVal = nums[i]
                maxLen = size
                maxIdx = i

        # caculate the result
        res = [maxVal]
        for i in range(maxIdx-1, -1, -1):
            if dp[i] == maxLen-1 and maxVal % nums[i] == 0:
                res.append(nums[i])
                maxLen -= 1
                maxVal = nums[i]

        return res

nums = [1,2,4,8]
obj = Solution()
print(obj.largestDivisibleSubset(nums))
