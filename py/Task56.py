from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort()
        res = []
        pre = intervals[0]
        for cur in intervals[1:]:
            if pre[1] < cur[0]:
                res.append(pre)
                pre = cur
            else:
                pre[1] = max(cur[1], pre[1])
        res.append(pre)
        return res
