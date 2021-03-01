from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        sums = [0]
        for num in nums:
            sums.append(num + sums[-1])
        self.sums = sums

    def sumRange(self, i: int, j: int) -> int:
        return self.sums[j+1] - self.sums[i]


# Your NumArray object will be instantiated and called as such:
nums = [-2, 0, 3, -5, 2, -1]
obj = NumArray(nums)
print(obj.sumRange(2, 5))
