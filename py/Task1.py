class Solution:
    def twoSum(self, nums:[int], target: int) -> [int]:
        dict = {}
        for idx,num in enumerate(nums):
            if num in dict:
                return [dict[num],idx]
            else:
                dict[target-num] = idx

solution = Solution()
print(solution.twoSum([2, 7, 11, 15],9))
