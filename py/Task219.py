from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        map = {}
        for idx, num in enumerate(nums):
            if num in map and idx-map[num] <= k:
                return True
            map[num] = idx
        return False

    def containsNearbyDuplicate2(self, nums: List[int], k: int) -> bool:
        keys = set()
        for idx, num in enumerate(nums):
            if num in keys:
                return True
            keys.add(num)
            if len(keys) > k:
                keys.remove(nums[idx-k])
        return False
