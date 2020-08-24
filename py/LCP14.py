# 给定一个整数数组 nums ，小李想将 nums 切割成若干个非空子数组，使得每个子数组最左边的数和最右边的数的最大公约数大于 1 。为了减少他的工作量，请求出最少可以切成多少个子数组。

# 示例 1：

# 输入：nums = [2,3,3,2,3,3]

# 输出：2

# 解释：最优切割为 [2,3,3,2] 和 [3,3] 。第一个子数组头尾数字的最大公约数为 2 ，第二个子数组头尾数字的最大公约数为 3 。

# 示例 2：

# 输入：nums = [2,3,5,7]

# 输出：4

# 解释：只有一种可行的切割：[2], [3], [5], [7]

# 限制：

# 1 <= nums.length <= 10^5
# 2 <= nums[i] <= 10^6

from typing import List

max_num = 10**6
min_factor = [1] * (max_num + 1)
for p in range(2, max_num+1):
    if min_factor[p] != 1:
        continue
    i = p
    while i * p <= max_num:
        if min_factor[i*p] == 1:
            min_factor[i*p] = p
        i += 1


class Solution:
    # recursion : brute-force
    # time out
    def splitArray(self, nums: List[int]) -> int:
        n = len(nums)

        def gcd(a: int, b: int) -> int:
            if b == 0:
                return a
            return gcd(b, a % b)

        def dfs(i: int, j: int) -> int:
            if i > j:
                return 0
            if gcd(nums[i], nums[j]) > 1:
                return 1
            res = j - i + 1
            for p in range(i, j):
                res = min(res, dfs(i, p)+dfs(p+1, j))
            return res
        return dfs(0, n-1)

    # recursion + memo
    # time out
    def splitArray2(self, nums: List[int]) -> int:
        n = len(nums)

        def gcd(a: int, b: int) -> int:
            if b == 0:
                return a
            return gcd(b, a % b)

        memo = {}

        def dfs(i: int, j: int) -> int:
            if i > j:
                return 0
            idx = i * n + j
            if idx in memo:
                return memo[idx]
            if gcd(nums[i], nums[j]) > 1:
                memo[idx] = 1
                return 1
            res = j - i + 1
            for p in range(i, j):
                res = min(res, dfs(i, p)+dfs(p+1, j))
            memo[idx] = res
            return res
        return dfs(0, n-1)

    # dp + 质数筛
    def splitArray3(self, nums: List[int]) -> int:
        prev = 0
        dp = {}
        for num in nums:
            cur = prev+1
            # 有质数因子
            while min_factor[num] != 1:
                factor = min_factor[num]
                dp[factor] = min(dp.get(factor, 10**6), prev+1)
                cur = min(cur, dp[factor])
                num //= factor
            # 质数
            dp[num] = min(dp.get(num, 10**6), prev+1)
            cur = min(cur, dp[num])
            prev = cur
        return prev


nums = [326614, 489921]
obj = Solution()
print(obj.splitArray3(nums))
