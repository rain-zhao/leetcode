from typing import List


class Solution:
    # brute force with recursion
    def maxCoins(self, nums: List[int]) -> int:
        def dfs(nums: List[int]) -> int:
            if not nums:
                return 0
            l = len(nums)
            res = 0
            for i in range(l):
                numLeft = nums[i - 1] if i > 0 else 1
                numRight = nums[i + 1] if i < l - 1 else 1
                nums0 = nums[:i] + nums[i+1:]
                res0 = nums[i] * numLeft * numRight + dfs(nums0)
                res = max(res, res0)
            return res
        return dfs(nums)

    # recursion + memo
    def maxCoins2(self, nums: List[int]) -> int:
        memo = {'[]': 0}

        def dfs(nums: List[int]) -> int:
            if str(nums) in memo:
                return memo[str(nums)]
            l = len(nums)
            res = 0
            for i in range(l):
                numLeft = nums[i - 1] if i > 0 else 1
                numRight = nums[i + 1] if i < l - 1 else 1
                nums0 = nums[:i] + nums[i+1:]
                res0 = nums[i] * numLeft * numRight + dfs(nums0)
                res = max(res, res0)
            memo[str(nums)] = res
            return res
        return dfs(nums)

    # cursion + memo 优化 ，倒过来操作，插入而非戳爆
    def maxCoins3(self, nums: List[int]) -> int:
        l = len(nums)
        memo = {}

        def dfs(i: int, j: int) -> int:
            if i > j:
                return 0
            idx = i * l + j
            if idx in memo:
                return memo[idx]
            res = 0
            numLeft = nums[i-1] if i > 0 else 1
            numRight = nums[j + 1] if j < l - 1 else 1
            for p in range(i, j + 1):
                res0 = nums[p] * numLeft * numRight + dfs(i, p-1) + dfs(p+1, j)
                res = max(res, res0)
            memo[idx] = res
            return res
        return dfs(0, l - 1)

    # dp
    def maxCoins4(self, nums: List[int]) -> int:
        if not nums:
            return 0
        l = len(nums)
        nums = [1] + nums + [1]
        # define & init
        dp = [[0] * (l+2) for _ in range(l+2)]
        # loop
        for k in range(l):
            for i in range(1, l - k + 1):
                j = i + k
                for p in range(i, j + 1):
                    res0 = nums[i-1] * nums[p] * \
                        nums[j+1] + dp[i][p-1] + dp[p+1][j]
                    dp[i][j] = max(dp[i][j], res0)
        return dp[1][l]


nums = [3, 1, 5, 8]
obj = Solution()
print(obj.maxCoins4(nums))
