from typing import List
from collections import Counter


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        cnts = {}
        for i in nums:
            cnts[i] = cnts.get(i, 0)+1
        items = tuple(cnts.items())
        res = []

        def dfs(seq, items, idx):
            if idx == len(items):
                res.append(seq)
                return
            key, val = items[idx]
            for i in range(val+1):
                dfs(seq+i*[key], items, idx+1)

        dfs([], items, 0)
        return res

    # iteration
    def subsetsWithDup2(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = [[]]
        i, n = 0, len(nums)
        while i < n:
            num = nums[i]
            count = 1
            i += 1
            while i < n and nums[i] == num:
                count += 1
                i += 1
            for candidate in res[:]:
                for cnt in range(1, count+1):
                    res.append(candidate + [num]*cnt)
        return res

    # iteration + using counter
    def subsetsWithDup3(self, nums: List[int]) -> List[List[int]]:
        counter = Counter(nums)
        res = [[]]
        for key in counter:
            count = counter[key]
            for candidate in res[:]:
                for i in range(1, count+1):
                    res.append(candidate + [key] * i)
        return res


nums = [1, 2, 2]
so = Solution()
print(so.subsetsWithDup3(nums))
