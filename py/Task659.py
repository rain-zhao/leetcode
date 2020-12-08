from typing import List
from collections import defaultdict
import heapq


class Solution:
    # hash + min-heap
    def isPossible(self, nums: List[int]) -> bool:
        map = defaultdict(list)
        for num in nums:
            prevLength = 0
            if map[num-1]:
                # pop min val from from heap
                prevLength = heapq.heappop(map[num-1])
            heapq.heappush(map[num], prevLength+1)
        return not any(item and item[0] < 3 for item in map.values())

    def isPossible2(self, nums: List[int]) -> bool:
        pre1, pre2, pre3 = 0, 0, 0
        n = len(nums)
        i = 0
        pre, cur = None, nums[0]-1
        while i < n:
            pre, cur = cur, nums[i]
            # calculate cnt
            cnt = 0
            while i < n and nums[i] == cur:
                cnt += 1
                i += 1
            # 当前数字跟前一位数字不连续
            if cur - pre > 1:
                if pre1 or pre2:
                    return False
                pre1, pre2, pre3 = cnt, 0, 0
                continue
            # 不满足子序列要大于3要求
            if cnt < pre1 + pre2:
                return False
            remain = cnt - pre1 - pre2
            pre1, pre2, pre3 = max(0, remain - pre3),\
                pre1, pre2 + min(pre3, remain)
        return not pre1 and not pre2


nums = [1, 2, 3, 3, 4, 5]
obj = Solution()
print(obj.isPossible(nums))
