# 给定一个整型数组, 你的任务是找到所有该数组的递增子序列，递增子序列的长度至少是2。

# 示例:

# 输入: [4, 6, 7, 7]
# 输出: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4,7,7]]
# 说明:

# 给定数组的长度不会超过15。
# 数组中的整数范围是 [-100,100]。
# 给定数组中可能包含重复数字，相等的数字应该被视为递增的一种情况。

from typing import List


class Solution:
    # 二进制枚举 + hash
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        visited = set()
        res = []
        for mask in range(3, 1 << n):
            candidate = self.translate(mask, nums)
            hashVal = self.hash(candidate)
            if hashVal not in visited and self.check(candidate):
                visited.add(hashVal)
                res.append(candidate)
        return res

    def translate(self, mask: int, nums: List[int]) -> List[int]:
        idx, res = 0, []
        while mask:
            if mask & 1:
                res.append(nums[idx])
            mask >>= 1
            idx += 1
        return res

    def hash(self, nums: List[int]) -> int:
        hashVal = 0
        base, mod = 211, 1000000007
        for num in nums:
            hashVal = (hashVal * base + num + 101) % mod
        return hashVal

    def check(self, candidate: List[int]) -> bool:
        if len(candidate) < 2:
            return False
        for cur, next in zip(candidate, candidate[1:]):
            if cur > next:
                return False
        return True

    # dfs
    def findSubsequences2(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []

        def dfs(cur: int, candidate: List[int]):
            # terminator
            if cur == n:
                if len(candidate) > 1:
                    res.append(candidate[:])
                return

            # drill down
            # 1.not choose
            if not candidate or candidate[-1] != nums[cur]:
                dfs(cur + 1, candidate)

            # 2.choose
            if not candidate or candidate[-1] <= nums[cur]:
                candidate.append(nums[cur])
                dfs(cur + 1, candidate)
                # reverse
                candidate.pop()
        dfs(0, [])
        return res


nums = [4, 6, 7, 7]
# nums = [-100, -99, -98, -97, -96, -96]
obj = Solution()
print(obj.findSubsequences(nums))
