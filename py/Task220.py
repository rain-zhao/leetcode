from typing import List


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if t < 0:
            return False
        bucket = {}
        t = t+1
        def getId(num: int) -> int:
            return num // t if num > 0 else (num + 1) // t - 1

        for i, num in enumerate(nums):
            idx = getId(num)
            if idx in bucket:
                return True
            # left neibor
            if idx - 1 in bucket and num - bucket[idx-1] < t:
                return True
            # right neibor
            if idx + 1 in bucket and bucket[idx+1] - num < t:
                return True
            # put into bucket
            bucket[idx] = num
            if len(bucket) > k:
                del bucket[getId(nums[i-k])]


so = Solution()
nums = [-1,-1]
k = 1
t = -1
print(so.containsNearbyAlmostDuplicate(nums, k, t))
