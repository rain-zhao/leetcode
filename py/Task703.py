import heapq
from typing import List


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.pq = nums
        heapq.heapify(nums)
        while len(nums) > k:
            heapq.heappop(nums)

    def add(self, val: int) -> int:
        if len(self.pq) < self.k:
            heapq.heappush(val)
        elif self.pq[0] < val:
            heapq.heapreplace(self.pq, val)

        return self.pq[0]
