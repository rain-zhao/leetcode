class Solution:
    def removeDuplicates(self, nums: [int]) -> int:
        if len(nums) < 2:
            return len(nums)
        pos = 2
        for num in nums[2:]:
            if num != nums[pos-2]:
                nums[pos] = num
                pos += 1
        return pos


so = Solution()
nums = [1,1,1,2,2,3]
print(so.removeDuplicates(nums))
