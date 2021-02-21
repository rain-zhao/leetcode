from typing import List
from collections import deque
from sortedcontainers import SortedList


class Solution:
    # using deque record max-items and min-items
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxQueue = deque()
        minQueue = deque()
        left = 0
        res = 0
        for right, num in enumerate(nums):
            while maxQueue and maxQueue[-1] < num:
                maxQueue.pop()
            maxQueue.append(num)
            while minQueue and minQueue[-1] > num:
                minQueue.pop()
            minQueue.append(num)
            while maxQueue[0] - minQueue[0] > limit:
                if nums[left] == maxQueue[0]:
                    maxQueue.popleft()
                elif nums[left] == minQueue[0]:
                    minQueue.popleft()
                left += 1
            res = max(res, right-left+1)
        return res

    # using sort container
    def longestSubarray2(self, nums: List[int], limit: int) -> int:
        sl = SortedList()
        left = 0
        res = 0
        for right, num in enumerate(nums):
            sl.add(num)
            while sl[-1] - sl[0] > limit:
                sl.remove(nums[left])
                left += 1
            res = max(res, right-left+1)
        return res


nums = [8, 2, 4, 7]
limit = 4
obj = Solution()
print(obj.longestSubarray(nums, limit))
