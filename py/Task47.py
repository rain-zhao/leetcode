from typing import List
from collections import Counter


class Solution:
    # dfs
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(nums: List[int], candidate: List[int]):
            if not nums:
                res.append(candidate)
                return
            # drill down
            dfs(nums[1:], candidate + [nums[0]])
            for i in range(1, len(nums)):
                if nums[i] == nums[i-1]:
                    continue
                dfs(nums[:i]+nums[i+1:], candidate + [nums[i]])
        dfs(nums, [])
        return res

    # dfs optimize code
    def permuteUnique2(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        counter = Counter(nums)
        candidate = []

        def dfs():
            if len(candidate) == n:
                res.append(candidate[:])
                return
            for num in counter:
                if not counter[num]:
                    continue
                counter[num] -= 1
                candidate.append(num)
                dfs()
                candidate.pop()
                counter[num] += 1
        dfs()
        return res


nums = [1, 1, 2]
obj = Solution()
print(obj.permuteUnique2(nums))
