from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1 or nums[0] < nums[-1]:
            return nums[0]
        left, right = 0, len(nums)-1
        while left <= right:
            mid = left + (right-left)//2
            if nums[mid] > nums[mid+1]:
                return nums[mid+1]
            elif nums[mid] >= nums[left]:
                left = mid+1
            else:
                right = mid-1
        return -1

    def findMin2(self, nums: List[int]) -> int:
        if (l:=len(nums)) == 1:
            return nums[0]
        left, right = 0, l - 1
        while left <= right:
            mid = (left + right) >> 1
            if nums[mid] < nums[mid - 1]:
                return nums[mid]
            elif nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid - 1
        return -1


nums = [4, 5, 1, 2, 3]
so = Solution()
print(so.findMin(nums))
