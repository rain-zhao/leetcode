from typing import List


class Solution:
    # iteration
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        occur = set()
        n = len(nums)
        for i in range(n-3):
            numi = nums[i]
            for j in range(i+1, n-2):
                numj = nums[j]
                map = {}
                for k in range(j+1, n):
                    numk = nums[k]
                    if numk in map and str(map[numk]+[numk]) not in occur:
                        res.append(map[numk]+[numk])
                        occur.add(str(res[-1]))
                    else:
                        map[target-numi-numj-numk] = [numi, numj, numk]
        return res

    # 左右指针
    def fourSum2(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)

        for i in range(n-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            if nums[i] << 2 > target:
                break
            if nums[i] + nums[-1] * 3 < target:
                continue
            for j in range(i+1, n-2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                if nums[i] + nums[j] * 3 > target:
                    break
                if nums[i] + nums[j] + (nums[-1] << 1) < target:
                    continue
                left, right = j+1, n-1
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    if total == target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left+1]:
                            left += 1
                        left += 1
                        while left < right and nums[right] == nums[right-1]:
                            right -= 1
                        right -= 1
                    elif total < target:
                        while left < right and nums[left] == nums[left+1]:
                            left += 1
                        left += 1
                    else:
                        while left < right and nums[right] == nums[right-1]:
                            right -= 1
                        right -= 1
        return res


nums = [-5, 5, 4, -3, 0, 0, 4, -2]
target = 4
obj = Solution()
print(obj.fourSum2(nums, target))
