from typing import List
from collections import defaultdict


class Solution:
    # dp
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        res = 1
        map = defaultdict(int)
        for val in arr:
            map[val] = map[val - difference] + 1
            res = max(res, map[val])
        return res


obj = Solution()
arr = [1,5,7,8,5,3,4,2,1]
difference = -2
print(obj.longestSubsequence(arr, difference))
