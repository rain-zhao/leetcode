from typing import List
from bisect import bisect


class Solution:
    # binary search
    def findBestValue(self, arr: List[int], target: int) -> int:
        if sum(arr) <= target:
            return max(arr)

        arr.sort()
        l = len(arr)
        prefix = [0]
        for num in arr:
            prefix.append(prefix[-1] + num)

        left, right = target // l, max(arr)
        while left <= right:
            mid = (left + right) >> 1
            it = bisect(arr, mid)
            cur = prefix[it] + mid * (l - it)
            if cur == target:
                return mid
            elif cur < target:
                left = mid + 1
            else:
                right = mid - 1

        def check(x):
            it = bisect(arr, x)
            return prefix[it] + x * (l - it)

        sumL = check(right)
        sumH = check(right + 1)

        return right if abs(sumL - target) <= abs(sumH - target) else right + 1

    def findBestValue2(self, arr: List[int], target: int) -> int:
        arr.sort()
        if sum(arr) <= target:
            return arr[-1]
        preSum = 0
        l = len(arr)
        for i in range(l):
            remainAvg = (target - preSum) / (l - i)
            if remainAvg <= arr[i]:
                it = int(remainAvg)
                if remainAvg - it <= 0.5:
                    return it
                else:
                    return it + 1
            preSum += arr[i]
        return arr[-1]


obj = Solution()
arr = [4, 9, 3]
target = 10
print(obj.findBestValue(arr, target))
