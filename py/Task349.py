from typing import List
from collections import Counter


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return set(nums1) & set(nums2)

    def intersection2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1, set2 = set(nums1), set(nums2)
        res = []
        for num in set1:
            if num in set2:
                res.append(num)
        return res


nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
so = Solution()
print(so.intersection2(nums1, nums2))
