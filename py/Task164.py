from typing import List


class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if not nums or len(nums) < 2:
            return 0
        nums.sort()
        res = 0
        for i, j in zip(nums, nums[1:]):
            res = max(res, j-i)
        return res

    def maximumGap2(self, nums: List[int]) -> int:
        if not nums or len(nums) < 2:
            return 0
        maxVal = max(nums)
        exp = 1
        aux = [0] * len(nums)
        while exp <= maxVal:
            count = [0] * 10
            # 1 count num
            for num in nums:
                count[num // exp % 10] += 1
            # 2 sum count
            for i in range(1, len(count)):
                count[i] += count[i-1]
            # 3 re-order
            for num in nums[::-1]:
                idx = num // exp % 10
                count[idx] -= 1
                aux[count[idx]] = num
            # loop
            aux, nums = nums, aux
            exp *= 10
        res = 0
        for i, j in zip(nums, nums[1:]):
            res = max(res, j-i)
        return res

    def maximumGap3(self, nums: List[int]) -> int:
        if not nums or len(nums) < 2:
            return 0
        mini, maxi = min(nums), max(nums)
        bucketSize = max(1, (maxi-mini)/(len(nums)-1))
        bucketNum = (maxi-mini)/bucketSize + 1
        buckets = [None] * int(bucketNum)

        for num in nums:
            idx = (num-mini)//bucketSize
            if not buckets[idx]:
                buckets[idx] = [num, num]
            else:
                # [minval,maxVal]
                buckets[idx][0], buckets[idx][1] = \
                    min(buckets[idx][0], num), max(buckets[idx][1], num)
        preMax, res = mini, 0
        for bucket in buckets:
            if not bucket:
                continue
            res = max(res, bucket[0]-preMax)
            preMax = bucket[1]
        return res


nums = [3, 6, 9, 1]
so = Solution()
print(so.maximumGap3(nums))
