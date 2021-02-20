from typing import List
from collections import Counter


class Solution:
    # hash + slide window
    def findShortestSubArray(self, nums: List[int]) -> int:
        degree = max(Counter(nums).values())
        left = 0
        res = len(nums)
        counter = Counter()
        for right, num in enumerate(nums):
            counter[num] += 1
            if counter[num] == degree:
                while nums[left] != num:
                    counter[nums[left]] -= 1
                    left += 1
                res = min(res, right-left+1)
        return res

    # hash 记录left，right
    def findShortestSubArray2(self, nums: List[int]) -> int:
        map = dict()
        for i, num in enumerate(nums):
            if num in map:
                map[num][0] += 1
                map[num][2] = i
            else:
                map[num] = [1, i, i]
        maxCnt = 0
        res = len(nums)
        for cnt, left, right in map.values():
            if cnt > maxCnt:
                maxCnt = cnt
                res = right - left + 1
            elif cnt == maxCnt:
                res = min(res, right - left + 1)
        return res


nums = [1, 2, 2, 3, 1]
obj = Solution()
print(obj.findShortestSubArray2(nums))
