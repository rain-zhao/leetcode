from typing import List


class Solution:
    # bucket sort
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        cnts = [0] * 101
        for num in nums:
            cnts[num] += 1
        for i in range(1, 101):
            cnts[i] += cnts[i-1]
        res = []
        for num in nums:
            res.append(cnts[num-1] if num else 0)
        return res


nums = [5, 0, 10, 0, 10, 6]
obj = Solution()
print(obj.smallerNumbersThanCurrent(nums))
