from typing import List


class Solution:
    def minTime(self, time: List[int], m: int) -> int:
        if len(time) <= m:
            return 0
        if m == 1:
            return sum(time) - max(time)

        def check(limit: int) -> bool:
            used = 1
            curMax = time[0]
            cur = 0
            for t in time[1:]:
                if cur + min(curMax, t) <= limit:
                    cur += min(curMax, t)
                    curMax = max(curMax, t)
                else:
                    used += 1
                    curMax = t
                    cur = 0
            return used <= m

        left, right = 0, sum(time)
        while left <= right:
            mid = (left + right) >> 1
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left


time = [1, 2, 3, 3]
m = 2
obj = Solution()
print(obj.minTime(time, m))
