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

    # 2021-04-07
    def search2(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        if n <= 8:
            return target in nums

        # 1 find min idx,题目已经保证数组已经经过旋转
        left, right = 0, n-2
        shift = -1
        while left <= right:
            mid = (left + right) >> 1
            if nums[mid] > nums[mid+1]:
                shift = mid + 1
                break
            elif nums[mid] < nums[left]:
                right = mid - 1
            elif nums[mid] > nums[left]:
                left = mid + 1
            else:
                left += 1

        if nums[shift] > target or nums[shift-1] < target:
            return False

        # binary search
        left, right = shift, n - 1 + shift
        while left <= right:
            mid = (left + right) >> 1
            if nums[mid % n] == target:
                return True
            elif nums[mid % n] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
