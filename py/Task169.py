from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if not nums:
            return 0
        cur, count = nums[0], 1
        for num in nums[1:]:
            if num == cur:
                count += 1
            elif count == 0:
                cur, count = num, 1
            else:
                count -= 1
        return cur
