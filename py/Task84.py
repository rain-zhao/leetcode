from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        l = len(heights)
        res = 0
        stack = [-1]

        for i in range(l):
            height = heights[i]
            while len(stack) > 1 and heights[stack[-1]] > height:
                res = max(res, heights[stack.pop()] * (i - stack[-1] - 1))
            stack.append(i)

        while len(stack) > 1:
            res = max(res, heights[stack.pop()] * (l - stack[-1] - 1))

        return res


obj = Solution()
heights = [2, 1, 5, 6, 2, 3]
print(obj.largestRectangleArea(heights))
