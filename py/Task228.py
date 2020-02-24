from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        if len(nums) == 1:
            return [str(nums[0])]
        res = []
        delta = 0
        for i, j in zip(nums, nums[1:]):
            if i == j-1:
                delta += 1
            else:
                res.append(str(i) if not delta else str(i-delta)+'->'+str(i))
                delta = 0
        res.append(str(j) if not delta else str(j-delta)+'->'+str(j))
        return res


so = Solution()
nums = [0, 2, 3, 4, 6, 8, 9]
print(so.summaryRanges(nums))
