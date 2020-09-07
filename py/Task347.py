# 给定一个非空的整数数组，返回其中出现频率前 k 高的元素。

#  

# 示例 1:

# 输入: nums = [1,1,1,2,2,3], k = 2
# 输出: [1,2]
# 示例 2:

# 输入: nums = [1], k = 1
# 输出: [1]
#  

# 提示：

# 你可以假设给定的 k 总是合理的，且 1 ≤ k ≤ 数组中不相同的元素的个数。
# 你的算法的时间复杂度必须优于 O(n log n) , n 是数组的大小。
# 题目数据保证答案唯一，换句话说，数组中前 k 个高频元素的集合是唯一的。
# 你可以按任意顺序返回答案。
from typing import List
from collections import Counter
from collections import _heapq


class Solution:
    # counter inner method
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [k for k, _ in Counter(nums).most_common(k)]

    # priority queue
    def topKFrequent2(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        pq = []
        for key in counter:
            if len(pq) < k:
                _heapq.heappush(pq, [counter[key], key])
            elif counter[key] > pq[0][0]:
                _heapq.heapreplace(pq, [counter[key], key])
        return [key for _, key in pq]

    # quick sort
    def topKFrequent3(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        array = list(counter)

        def quickSelect(beg: int, end: int):
            p = beg + 1
            for i in range(beg + 1, end + 1):
                if counter[array[i]] > counter[array[beg]]:
                    array[i], array[p] = array[p], array[i]
                    p += 1
            array[p-1], array[beg] = array[beg], array[p-1]
            if p == k:
                return
            elif p > k:
                quickSelect(beg, p - 1)
            else:
                quickSelect(p, end)

        quickSelect(0, len(array) - 1)
        return array[:k]


nums = [1, 1, 1, 2, 2, 3]
k = 2
obj = Solution()
print(obj.topKFrequent3(nums, k))
