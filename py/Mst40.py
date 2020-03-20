# 输入整数数组 arr ，找出其中最小的 k 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。


# 示例 1：

# 输入：arr = [3,2,1], k = 2
# 输出：[1,2] 或者 [2,1]
# 示例 2：

# 输入：arr = [0,1,2,1], k = 1
# 输出：[0]


# 限制：

# 0 <= k <= arr.length <= 10000
# 0 <= arr[i] <= 10000

from typing import List
import heapq


class Solution:
    # using heap
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if k == len(arr):
            return arr
        if k == 1:
            return [min(arr)]
        if k > len(arr)//2:
            arr = sorted(arr)
            return arr[:k]
        return heapq.nsmallest(k, arr)


obj = Solution()
arr = [3, 2, 1]
k = 2
print(obj.getLeastNumbers(arr, k))
