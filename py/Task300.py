from typing import List
import bisect


class Solution:
    # dp
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp[i] = 以第i个数字结尾的最长子序列
        dp = [1] * len(nums)
        for i, num in enumerate(nums):
            for j in range(i):
                if num > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)

    # stack + binary search
    def lengthOfLIS2(self, nums: List[int]) -> int:
        d = nums[:1]
        for num in nums[1:]:
            if num > d[-1]:
                d.append(num)
            else:
                # binary serch
                left, right = 0, len(d)-1
                while left <= right:
                    mid = (left+right) >> 1
                    if num > d[mid]:
                        left = mid + 1
                    else:
                        right = mid - 1
                d[left] = num
        return len(d)

    # # stack + binary search(using bisect liberary)
    def lengthOfLIS3(self, nums: List[int]) -> int:
        d = nums[:1]
        for num in nums[1:]:
            if num > d[-1]:
                d.append(num)
            else:
                d[bisect.bisect_left(d, num)] = num
        return len(d)


nums = [10, 9, 2, 5, 3, 7, 101, 18]
obj = Solution()
print(obj.lengthOfLIS3(nums))
