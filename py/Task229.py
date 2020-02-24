from typing import List
from collections import defaultdict


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []
        threadshold = len(nums)//3
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
        for k, v in counts.items():
            if v > threadshold:
                res.append(k)
        return res

    def majorityElement2(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        res = []
        major1, count1 = nums[0], 0
        major2, count2 = nums[0], 0
        for num in nums:
            if num == major1:
                count1 += 1
                continue
            if num == major2:
                count2 += 1
                continue
            if count1 == 0:
                major1, count1 = num, 1
                continue
            if count2 == 0:
                major2, count2 = num, 1
                continue
            count1 -= 1
            count2 -= 1
        count1 = count2 = 0
        for num in nums:
            if num == major1:
                count1+=1
            elif num == major2:
                count2+=1
        if count1 > len(nums)//3:
            res.append(major1)
        if count2 > len(nums)//3:
            res.append(major2)
        return res


nums = [1, 1, 1, 3, 3, 2, 2, 2]
so = Solution()
print(so.majorityElement(nums))
