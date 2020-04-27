from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        # [4,5,6,7,0,1,2]
        # find min idx
        shift = 0
        left, right = 0, len(nums)-1
        while left <= right:
            mid = left + (right-left) // 2
            if nums[mid] < nums[mid-1]:
                shift = mid
                break
            elif nums[mid] < nums[0]:
                right = mid - 1
            else:
                left = mid + 1
        # binary search
        left, right = 0, len(nums)-1
        while left <= right:
            mid = left + (right-left) // 2
            mm = (mid+shift) % len(nums)
            if nums[mm] == target:
                return mm
            elif nums[mm] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
    # 2020-04-27

    def search2(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        if len(nums) == 1:
            return 0 if nums[0] == target else -1

        shift = 0
        # [4,5,6,7,0,1,2]
        if nums[0] > nums[-1]:
            # binary search, find the min idx
            left, right = 0, len(nums) - 2
            while left <= right:
                mid = (left + right) >> 1
                if nums[mid] > nums[mid+1]:
                    shift = mid + 1
                    break
                elif nums[mid] < nums[left]:
                    right = mid - 1
                else:
                    left = mid + 1

        # find target
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left + right) >> 1
            mm = (mid+shift) % len(nums)
            if nums[mm] == target:
                return mm
            elif nums[mm] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1


so = Solution()
nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
print(so.search2(nums, target))
