
from typing import List


class Solution:
    def findLongestPath(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        max = []
        cur = nums[:1]
        for num in nums[1:]:
            if num == cur[-1]+1:
                cur.append(num)
            else:
                max = cur if len(cur) > len(max) else max
                cur = [num, ]
        max = cur if len(cur) > len(max) else max
        return max


nums = [3, 2, 4, 5, 6, 1, 9]
so = Solution()
print(so.findLongestPath(nums))
