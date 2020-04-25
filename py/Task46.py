from typing import List
from typing import Set


class Solution:
    # using set
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def _dfs(l: List[int], s: Set[int]):
            if not s:
                res.append(l)
                return
            for i in set(s):
                s.remove(i)
                _dfs(l+[i], s)
                s.add(i)

        _dfs([], set(nums))
        return res

    # using swap
    def permute2(self, nums: List[int]) -> List[List[int]]:
        res = []

        def _dfs(length: int):
            if length <= 1:
                res.append(nums[::])
                return
            for i in range(length):
                # swap idx's num and last num
                nums[i], nums[length-1] = nums[length-1], nums[i]
                _dfs(length-1)
                # backward
                nums[i], nums[length-1] = nums[length-1], nums[i]

        _dfs(len(nums))
        return res


obj = Solution()
nums = [1, 2, 3]
print(obj.permute2(nums))
