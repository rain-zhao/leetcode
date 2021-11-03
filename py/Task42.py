from typing import List


class Solution:
    # dp
    def trap(self, height: List[int]) -> int:
        n = len(height)
        lefts, rights = height[:], height[:]
        for i in range(1, n):
            lefts[i] = max(lefts[i], lefts[i-1])
            rights[n-1-i] = max(rights[n-1-i], rights[n-i])

        res = 0
        for i in range(1, n-1):
            res += min(lefts[i], rights[i]) - height[i]
        return res

    # monotone stack
    def trap4(self, height: List[int]) -> int:
        n = len(height)
        if n < 3:
            return 0

        stack = [0]
        res = 0
        for i in range(1, n):
            while height[stack[-1]] <= height[i]:
                ii = stack.pop()
                if not stack:
                    break
                x = i - stack[-1] - 1
                y = min(height[stack[-1]], height[i]) - height[ii]
                res += x * y
            stack.append(i)
        return res

    # double cursor
    def trap3(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        maxl, maxr = height[left], height[right]
        res = 0
        while left < right:
            if height[left] < height[right]:
                maxl = max(maxl, height[left])
                res += maxl - height[left]
                left += 1
            else:
                maxr = max(maxr, height[right])
                res += maxr - height[right]
                right -= 1
        return res


obj = Solution()
height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(obj.trap4(height))
