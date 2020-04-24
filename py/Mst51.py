# 在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组，求出这个数组中的逆序对的总数。

#  

# 示例 1:

# 输入: [7,5,6,4]
# 输出: 5
#  

# 限制：

# 0 <= 数组长度 <= 50000
from typing import List


class Solution:
    # merge sort
    def reversePairs(self, nums: List[int]) -> int:
        if not nums:
            return 0

        self.res = 0

        def merge(arr1: List[int], arr2: List[int]) -> List[int]:
            p1 = p2 = 0
            l = []
            while p1 < len(arr1) and p2 < len(arr2):
                if arr1[p1] <= arr2[p2]:
                    l.append(arr1[p1])
                    p1 += 1
                else:
                    self.res += len(arr1) - p1
                    l.append(arr2[p2])
                    p2 += 1

            while p1 < len(arr1):
                l.append(arr1[p1])
                p1 += 1
            while p2 < len(arr2):
                l.append(arr2[p2])
                p2 += 1
            return l

        def mergeSort(arr: List[int]) -> List[int]:
            if len(arr) <= 1:
                return arr
            mid = len(arr) >> 1
            left = mergeSort(arr[:mid])
            right = mergeSort(arr[mid:])
            return merge(left, right)

        mergeSort(nums)
        return self.res


nums = [7, 5, 6, 4]
obj = Solution()
print(obj.reversePairs(nums))
