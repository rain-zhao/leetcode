from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        nums[:] = nums[-k:]+nums[:-k]

    # reverse array,using user defined reverse method
    def rotate2(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n

        def reverse(nums: List[int], start: int, end: int) -> None:
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        reverse(nums, 0, n-1)
        reverse(nums, 0, k-1)
        reverse(nums, k, n-1)

    # using 1 temp value
    def rotate3(self, nums: List[int], k: int) -> None:
        n = len(nums)
        cnt = 0
        start = 0
        while cnt < n:
            cur = start
            prev = nums[start]
            while True:
                next = (cur + k) % n
                nums[next], prev = prev, nums[next]
                cur = next
                cnt += 1
                if cur == start:
                    break
            start += 1


nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
obj = Solution()
print(obj.rotate3(nums, k))
