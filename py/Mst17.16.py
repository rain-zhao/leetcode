# 一个有名的按摩师会收到源源不断的预约请求，每个预约都可以选择接或不接。在每次预约服务之间要有休息时间，因此她不能接受相邻的预约。给定一个预约请求序列，替按摩师找到最优的预约集合（总预约时间最长），返回总的分钟数。

# 注意：本题相对原题稍作改动

#  

# 示例 1：

# 输入： [1,2,3,1]
# 输出： 4
# 解释： 选择 1 号预约和 3 号预约，总时长 = 1 + 3 = 4。
# 示例 2：

# 输入： [2,7,9,3,1]
# 输出： 12
# 解释： 选择 1 号预约、 3 号预约和 5 号预约，总时长 = 2 + 9 + 1 = 12。
# 示例 3：

# 输入： [2,1,4,5,3,1,1,3]
# 输出： 12
# 解释： 选择 1 号预约、 3 号预约、 5 号预约和 8 号预约，总时长 = 2 + 4 + 3 + 3 = 12。

from typing import List


class Solution:
    # dp
    def massage(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        # define and init
        dp = [[0, 0] for _ in range(len(nums))]
        dp[0][0], dp[0][1] = nums[0], 0

        for idx, num in enumerate(nums[1:], 1):
            dp[idx][0], dp[idx][1] = dp[idx-1][1] + \
                num, max(dp[idx-1][0], dp[idx-1][1])

        return max(dp[-1])

    # dp 压缩空间
    def massage2(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        # define and init
        r1, r2 = nums[0], 0

        for num in nums[1:]:
            r1, r2 = r2 + num, max(r1, r2)

        return max(r1, r2)


obj = Solution()
nums = [1, 2, 3, 1]
print(obj.massage(nums))
