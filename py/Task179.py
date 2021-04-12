from typing import List
from functools import cmp_to_key


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def cmp(x: str, y: str) -> int:
            return -1 if x + y > y + x else 1
        nums = [str(num) for num in nums]
        nums.sort(key=cmp_to_key(cmp))
        res = ''.join(nums)
        if res[0] == '0':
            return '0'
        return res


nums = [3, 30, 34, 5, 9]
obj = Solution()
print(obj.largestNumber(nums))
