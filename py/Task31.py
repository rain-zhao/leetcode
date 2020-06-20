from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        l = len(nums)

        if l <= 1:
            return

        # find the last asc num
        i = l - 2
        while i > -1 and nums[i] >= nums[i + 1]:
            i -= 1

        if i == -1:
            nums.reverse()
            return

        # find the first j gt i
        j = l - 1
        while nums[j] <= nums[i]:
            j -= 1

        # swap
        nums[i], nums[j] = nums[j], nums[i]

        # reverse the tail
        i, j = i + 1, l-1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1


nums = [1, 2, 3]
obj = Solution()
print(obj.nextPermutation(nums))
