# 给定一个未排序的整数数组，找出最长连续序列的长度。

# 要求算法的时间复杂度为 O(n)。

# 示例:

# 输入: [100, 4, 200, 1, 3, 2]
# 输出: 4
# 解释: 最长连续序列是 [1, 2, 3, 4]。它的长度为 4。

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = set(nums)
        cnts = {}

        def dfs(num: int) -> int:
            # terminator
            if num not in nums:
                return 0
            if num in cnts:
                return cnts[num]
            cnts[num] = 1 + dfs(num-1)
            return cnts[num]

        res = 0
        for num in nums:
            res = max(res, dfs(num))

        return res

    def longestConsecutive2(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 0
        for num in nums:
            if num + 1 in nums:
                continue
            cur = num
            length = 0
            while cur in nums:
                cur -= 1
                length += 1

            res = max(res, length)
        return res


nums = [100, 4, 200, 1, 3, 2]
obj = Solution()
print(obj.longestConsecutive2(nums))
