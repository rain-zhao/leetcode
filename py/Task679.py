from typing import List


class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:

        def dfs(nums: List[int]) -> bool:
            if len(nums) == 1:
                return -0.01 < nums[0] - 24 < 0.01
            for num1 in nums[:]:
                nums.remove(num1)
                for num2 in nums[:]:
                    nums.remove(num2)
                    # add,剪枝，满足交换律，剪掉num1 < num2 的分支
                    if num1 >= num2 and dfs(nums + [num1+num2]):
                        return True
                    # multi，剪枝，满足交换律，剪掉num1 < num2 的分支
                    if num1 >= num2 and dfs(nums + [num1*num2]):
                        return True
                    # divide
                    if num2 > 0.01 and dfs(nums + [num1/num2]):
                        return True
                    # minus
                    if dfs(nums + [num1-num2]):
                        return True
                    # reset
                    nums.append(num2)
                # reset
                nums.append(num1)
            return False

        return dfs(nums)


nums = [4, 1, 8, 7]
obj = Solution()
print(obj.judgePoint24(nums))
