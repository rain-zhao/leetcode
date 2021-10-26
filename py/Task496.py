from typing import DefaultDict, List
from collections import defaultdict


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = defaultdict(lambda: -1)
        stack = []
        for num in nums2:
            while stack and num > stack[-1]:
                d[stack.pop()] = num
            stack.append(num)
        return [d[num] for num in nums1]


nums1 = [2, 4]
nums2 = [1, 2, 3, 4]
obj = Solution()
print(obj.nextGreaterElement(nums1, nums2))
