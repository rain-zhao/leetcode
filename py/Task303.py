from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        sum = [0]
        for num in nums:
            sum.append(num+sum[-1])
        self.sum = sum

    def sumRange(self, i: int, j: int) -> int:
        return self.sum[j+1] - self.sum[i]


# Your NumArray object will be instantiated and called as such:
nums = [-2, 0, 3, -5, 2, -1]
obj = NumArray(nums)
print(obj.sumRange(2, 5))
