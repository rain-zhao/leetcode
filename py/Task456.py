from typing import List
import bisect


class Solution:
    # brute-force(n3)
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] < nums[j]:
                    for k in range(j+1, n):
                        if nums[i] < nums[k] < nums[j]:
                            return True
        return False

    # sort array(n2)
    def find132pattern2(self, nums: List[int]) -> bool:
        n = len(nums)
        sortArr = nums[0:1]
        for j in range(1, n):
            numj = nums[j]
            bisect.insort_right(sortArr, numj)
            if numj > sortArr[0]:
                numi = sortArr[0]
                for k in range(j+1, n):
                    numk = nums[k]
                    if numi < numk < numj:
                        return True
        return False

    # 枚举3 和2 （n2）
    def find132pattern3(self, nums: List[int]) -> bool:
        n = len(nums)
        numi = nums[0]
        for j in range(1, n):
            numj = nums[j]
            if numi < numj:
                for k in range(j+1, n):
                    numk = nums[k]
                    if numi < numk < numj:
                        return True
            else:
                numi = numj
        return False

    # 单调栈
    def find132pattern4(self, nums: List[int]) -> bool:
        n = len(nums)
        minLeft = nums[0:1]
        for num in nums[1:]:
            minLeft.append(min(minLeft[-1], num))
        stack = []
        for j in range(n-1, 0, -1):
            numj = nums[j]
            numk = numi = minLeft[j]
            while stack and stack[-1] < numj:
                numk = stack.pop()
            if numk > numi:
                return True
            stack.append(numj)
        return False


nums = [1, 0, 1, -4, -3]
obj = Solution()
print(obj.find132pattern(nums))
