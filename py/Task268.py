from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        appears = [False] * (n+1)
        for num in nums:
            appears[num] = True
        for i, appear in enumerate(appears):
            if not appear:
                return i
        return 0

    def missingNumber2(self, nums: List[int]) -> int:
        n = len(nums)
        return n * (n+1) // 2 - sum(nums)

    def missingNumber3(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        for i in range(n+1):
            res ^= i
        for num in nums:
            res ^= num
        return res


obj = Solution()
nums = [3, 0, 1]
print(obj.missingNumber3(nums))
