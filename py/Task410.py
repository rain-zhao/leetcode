from typing import List


class Solution:
    # recursion + memo
    def splitArray(self, nums: List[int], m: int) -> int:
        N = len(nums)
        sub = [0, ]
        for num in nums:
            sub.append(sub[-1]+num)

        memo = {}

        def splitArray(n: int, m: int) -> int:
            if m == 1:
                return sub[n]
            idx = str(n)+','+str(m)
            if idx in memo:
                return memo[idx]
            res = 99999999999
            for i in range(m-1, n):
                res = min(res, max(splitArray(i, m-1), sub[n]-sub[i]))

            memo[idx] = res
            return res

        return splitArray(N, m)

    # dp
    def splitArray2(self, nums: List[int], m: int) -> int:
        if m == 1:
            return sum(nums)
        n = len(nums)
        sub = [0, ]
        for num in nums:
            sub.append(sub[-1]+num)
        # define
        dp = [[99999999999] * (m+1) for _ in range(n+1)]
        # init
        for i in range(n+1):
            dp[i][1] = sub[i]
        for j in range(2, m+1):
            for i in range(j, n+1):
                for k in range(j-1, i):
                    dp[i][j] = min(dp[i][j], max(dp[k][j-1], sub[i]-sub[k]))
        return dp[-1][-1]


obj = Solution()
nums = [7, 2, 5, 10, 8]
m = 2
print(obj.splitArray2(nums, m))
