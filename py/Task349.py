from typing import List
from collections import Counter


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return set(nums1) & set(nums2) 


nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
so = Solution()
print(so.intersection(nums1, nums2))
