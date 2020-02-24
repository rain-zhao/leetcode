from bisect import bisect_left


class Solution:
    def insert(self, intervals: [[int]], newInterval: [int]) -> [[int]]:
        if not intervals:
            return [newInterval]
        if intervals[0][0] > newInterval[1]:
            return [newInterval] + intervals
        if intervals[-1][1] < newInterval[0]:
            return intervals + [newInterval]
        res = []
        for idx, interval in enumerate(intervals):
            if interval[1] < newInterval[0]:
                res.append(interval)
            elif interval[0] <= newInterval[0]:
                newInterval = [interval[0], max(interval[1], newInterval[1])]
            elif interval[0] > newInterval[1]:
                res = res + [newInterval] + intervals[idx:]
                newInterval = None
                break
            else:
                newInterval[1] = max(interval[1], newInterval[1])

        if newInterval:
            res.append(newInterval)

        return res

    def insert2(self, intervals: [[int]], newInterval: [int]) -> [[int]]:
        pos = bisect_left(intervals, newInterval)
        res = []

        for interval in intervals[:pos]:
            if interval[1] < newInterval[0]:
                res.append(interval)
            else:
                newInterval = [interval[0], max(interval[1], newInterval[1])]

        for idx, interval in enumerate(intervals[pos:], pos):
            if newInterval[1] >= interval[0]:
                newInterval[1] = max(interval[1], newInterval[1])
            else:
                res += [newInterval]+intervals[idx:]
                return res
        res += [newInterval]
        return res

    def insert3(self, intervals: [[int]], newInterval: [int]) -> [[int]]:
        if not intervals:
            return [newInterval]
        intervals.append(newInterval)
        intervals.sort()
        res = []
        res.append(intervals[0])

        for interval in intervals[1:]:
            if res[-1][1] < interval[0]:
                res.append(interval)
            else:
                res[-1][1] = max(res[-1][1],interval[1])
        return res


solution = Solution()
intervals = [[1, 3], [6, 9]]
newInterval = [2, 5]
print(solution.insert3(intervals, newInterval))
