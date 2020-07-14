from typing import List


class Solution:
    # brute force o(n2)
    def countSmaller(self, nums: List[int]) -> List[int]:
        l = len(nums)
        res = [0] * l
        for i in range(l):
            num1 = nums[i]
            for j in range(i+1, l):
                num2 = nums[j]
                if num1 > num2:
                    res[i] += 1
        return res

    # merge sort,最简单实现，不使用公共数组
    def countSmaller2(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        l = len(nums)
        res = [0] * l
        arr = [i for i in range(l)]

        def mergeSort(nums: List[int]) -> List[int]:
            if len(nums) < 2:
                return nums
            mid = len(nums) >> 1
            arr1 = mergeSort(nums[:mid])
            arr2 = mergeSort(nums[mid:])
            return merge(arr1, arr2)

        def merge(arr1: List[int], arr2: List[int]) -> List[int]:
            l1, l2 = len(arr1), len(arr2)
            p1, p2, p3 = l1 - 1, l2 - 1, l1 + l2 - 1
            arr3 = [0] * (l1 + l2)

            while p1 >= 0 and p2 >= 0:
                if nums[arr1[p1]] > nums[arr2[p2]]:
                    res[arr1[p1]] += p2 + 1
                    arr3[p3] = arr1[p1]
                    p1 -= 1
                    p3 -= 1
                else:
                    arr3[p3] = arr2[p2]
                    p2 -= 1
                    p3 -= 1
            while p1 >= 0:
                arr3[p3] = arr1[p1]
                p1 -= 1
                p3 -= 1
            while p2 >= 0:
                arr3[p3] = arr2[p2]
                p2 -= 1
                p3 -= 1
            return arr3

        mergeSort(arr)
        return res

    # merge sort with 公共数组
    def countSmaller3(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        l = len(nums)
        res = [0] * l

        sortIdx = [i for i in range(l)]
        cache = sortIdx[::]

        def mergeSort(beg: int, end: int):
            if beg == end:
                return
            mid = (beg + end) >> 1
            mergeSort(beg, mid)
            mergeSort(mid+1, end)
            merge(beg, end)

        def merge(beg: int, end: int):
            cache[beg:end+1] = sortIdx[beg:end+1]
            mid = (beg + end) >> 1
            p1, p2, p3 = mid, end, end
            while p1 >= beg and p2 > mid:
                if nums[cache[p1]] > nums[cache[p2]]:
                    res[cache[p1]] += p2 - mid
                    sortIdx[p3] = cache[p1]
                    p1 -= 1
                    p3 -= 1
                else:
                    sortIdx[p3] = cache[p2]
                    p2 -= 1
                    p3 -= 1
            while p1 >= beg:
                sortIdx[p3] = cache[p1]
                p1 -= 1
                p3 -= 1
            while p2 > mid:
                sortIdx[p3] = cache[p2]
                p2 -= 1
                p3 -= 1

        mergeSort(0, l - 1)
        return res


obj = Solution()
nums = [5, 2, 6, 1]
print(obj.countSmaller3(nums))
