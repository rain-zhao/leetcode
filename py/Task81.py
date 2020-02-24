from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums:
            return False
        if len(nums) == 1:
            return nums[0] == target
        # [2,5,6,0,0,1,2]
        # find min idx
        shift = 0
        left, right = 0, len(nums)-2
        while left <= right:
            mid = left + (right-left) // 2
            if nums[mid] > nums[mid+1]:
                shift = mid+1
                break
            elif nums[mid] < nums[left]:
                right = mid - 1
            elif nums[mid] > nums[left]:
                left = mid + 1
            else:
                left += 1
        # binary search
        left, right = 0, len(nums)-1
        while left <= right:
            mid = left + (right-left) // 2
            mm = (mid+shift) % len(nums)
            if nums[mm] == target:
                return True
            elif nums[mm] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
