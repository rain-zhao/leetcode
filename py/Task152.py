from typing import List


class Solution:
    # dp
    def maxProduct(self, nums: List[int]) -> int:
        res = mmin = mmax = nums[0]
        for num in nums[1:]:
            if not num:
                mmin = mmax = 0
            elif num > 0:
                mmin, mmax = min(num, mmin * num), max(num, mmax * num)
            else:
                mmin, mmax = min(num, mmax * num), max(num, mmin * num)

            res = max(res, mmax)
        return res


nums = [2, 3, -2, 4]
obj = Solution()
print(obj.maxProduct(nums))
