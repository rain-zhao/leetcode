from typing import List
import heapq


class Solution:
    # priority queue
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq = [nums[0], ]
        for num in nums[1:]:
            if len(pq) < k:
                heapq.heappush(pq, num)
            elif pq[0] < num:
                heapq.heapreplace(pq, num)
        return pq[0]

    def findKthLargest2(self, nums: List[int], k: int) -> int:
        def quickselect(nums: List[int], beg: int, end: int) -> int:
            pivot = beg
            for i in range(beg, end):
                if nums[i] < nums[end]:
                    nums[i], nums[pivot] = nums[pivot], nums[i]
                    pivot += 1
            nums[end], nums[pivot] = nums[pivot], nums[end]
            return pivot
        i, j = 0, len(nums)-1
        target = len(nums)-k
        pivot = quickselect(nums, i, j)
        while pivot != target:
            if pivot > target:
                j = pivot-1
                pivot = quickselect(nums, i, j)
            else:
                i = pivot+1
                pivot = quickselect(nums, i, j)
        return nums[pivot]

    def findKthLargest3(self, nums: List[int], k: int) -> int:
        # seperate the list by end item
        def quickSelect(beg: int, end: int) -> int:
            pivot = beg
            for i in range(beg, end):
                if nums[i] < nums[end]:
                    nums[i], nums[pivot] = nums[pivot], nums[i]
                    pivot += 1
            nums[pivot], nums[end] = nums[end], nums[pivot]
            return pivot
        target = len(nums) - k
        beg, end = 0, len(nums)-1
        while True:
            pivot = quickSelect(beg, end)
            if pivot == target:
                return nums[pivot]
            elif pivot < target:
                beg = pivot + 1
            else:
                end = pivot - 1
        return nums[pivot]

    # priority queue
    def findKthLargest4(self, nums: List[int], k: int) -> int:
        pq = nums[:k]
        heapq.heapify(pq)
        for num in nums[k:]:
            if pq[0] < num:
                heapq.heapreplace(pq, num)
        return pq[0]


nums = [3, 2, 1, 5, 6, 4]
k = 2
so = Solution()
print(so.findKthLargest2(nums, k))
