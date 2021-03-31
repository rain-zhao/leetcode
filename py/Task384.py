from typing import List
import random


class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def reset(self) -> List[int]:
        return self.nums

    # def shuffle(self) -> List[int]:
    #     rand = self.nums[:]
    #     n = len(rand)
    #     for i in range(n):
    #         idx = random.randrange(i, n)
    #         rand[idx], rand[i] = rand[i], rand[idx]
    #     return rand

    def shuffle(self) -> List[int]:
        rand = self.nums[:]
        n = len(rand)
        for i in range(n-1, -1, 0):
            idx = random.randint(0, i)
            rand[idx], rand[i] = rand[i], rand[idx]
        return rand

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
