# 你有 k 个升序排列的整数数组。找到一个最小区间，使得 k 个列表中的每个列表至少有一个数包含在其中。

# 我们定义如果 b-a < d-c 或者在 b-a == d-c 时 a < c，则区间 [a,b] 比 [c,d] 小。

# 示例 1:

# 输入:[[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
# 输出: [20,24]
# 解释:
# 列表 1：[4, 10, 15, 24, 26]，24 在区间 [20,24] 中。
# 列表 2：[0, 9, 12, 20]，20 在区间 [20,24] 中。
# 列表 3：[5, 18, 22, 30]，22 在区间 [20,24] 中。
# 注意:

# 给定的列表可能包含重复元素，所以在这里升序表示 >= 。
# 1 <= k <= 3500
# -105 <= 元素的值 <= 105
# 对于使用Java的用户，请注意传入类型已修改为List<List<Integer>>。重置代码模板后可以看到这项改动。


from typing import List
import heapq
from collections import defaultdict


class Solution:
    # priority queue
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        pq = [[subList[0], i, 0] for i, subList in enumerate(nums)]
        maxVal = max(pq)[0]
        heapq.heapify(pq)
        left, right = -10**5, 10**5
        while True:
            minVal, i, j = pq[0]
            subList = nums[i]
            if maxVal - minVal < right - left:
                left, right = minVal, maxVal
            j += 1
            if j >= len(subList):
                break
            maxVal = max(maxVal, subList[j])
            heapq.heapreplace(pq, [subList[j], i, j])
        return [left, right]

    # slide window
    def smallestRange2(self, nums: List[List[int]]) -> List[int]:
        k = len(nums)
        indices = defaultdict(list)
        for i, subList in enumerate(nums):
            for v in subList:
                indices[v].append(i)
        valList = sorted(indices)
        left, right = 0, 0
        resLeft, resRight = valList[0], valList[-1]
        need = [1] * k
        needCnt = k
        while right < len(valList):
            for idx in indices[valList[right]]:
                need[idx] -= 1
                if need[idx] == 0:
                    needCnt -= 1
            while needCnt == 0:
                if valList[right] - valList[left] < resRight - resLeft:
                    resLeft, resRight = valList[left], valList[right]
                for idx in indices[valList[left]]:
                    need[idx] += 1
                    if need[idx] == 1:
                        needCnt += 1
                left += 1
            right += 1
        return [resLeft, resRight]


obj = Solution()
nums = [[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]]
print(obj.smallestRange2(nums))
