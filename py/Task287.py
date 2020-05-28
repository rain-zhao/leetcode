from typing import List


class Solution:
    # 1.hash
    def findDuplicate(self, nums: List[int]) -> int:
        array = [0] * len(nums)
        for num in nums:
            if array[num]:
                return num
            array[num] = 1

    # Floyd
    def findDuplicate2(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return nums[0]

        # fist loop
        p1, p2 = nums[0], nums[nums[0]]
        while p1 != p2:
            p1, p2 = nums[p1], nums[nums[p2]]

        # 2ed loop
        p1 = 0
        while p1 != p2:
            p1, p2 = nums[p1], nums[p2]

        return p1

    # binary search
    def findDuplicate3(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return nums[0]
        l = len(nums)
        left, right = 1, l-1
        while left <= right:
            mid = (left + right) >> 1

            cnt = 0
            for num in nums:
                cnt += 1 if num <= mid else 0

            if cnt <= mid:
                left = mid + 1
            else:
                right = mid - 1

        return left
