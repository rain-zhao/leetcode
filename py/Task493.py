from typing import List
import bisect


class Solution:
    # 二分法 (可用红黑树or跳表优化插入性能)
    def reversePairs(self, nums: List[int]) -> int:
        sortedArr = []
        res = 0
        for num in nums[::-1]:
            idx = bisect.bisect_left(sortedArr, num)
            res += idx
            bisect.insort(sortedArr, num*2)
        return res

    # merge-sort
    def reversePairs2(self, nums: List[int]) -> int:

        def reversePairsRecur(i: int, j: int) -> int:
            if i >= j:
                return 0
            mid = (i+j) >> 1
            res = reversePairsRecur(i, mid)
            res += reversePairsRecur(mid+1, j)
            # 计算本层产生的翻转对
            p1, p2 = i, mid+1
            while p1 <= mid and p2 <= j:
                if nums[p1] > 2 * nums[p2]:
                    res += mid - p1 + 1
                    p2 += 1
                else:
                    p1 += 1
            # 归并
            tmp = []
            p1, p2 = i, mid+1
            while p1 <= mid and p2 <= j:
                if nums[p1] < nums[p2]:
                    tmp.append(nums[p1])
                    p1 += 1
                else:
                    tmp.append(nums[p2])
                    p2 += 1
            while p1 <= mid:
                tmp.append(nums[p1])
                p1 += 1
            while p2 <= j:
                tmp.append(nums[p2])
                p2 += 1
            nums[i:j+1] = tmp
            return res
        return reversePairsRecur(0, len(nums)-1)


nums = [2, 4, 3, 5, 1]
obj = Solution()
print(obj.reversePairs2(nums))
