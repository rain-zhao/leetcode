from typing import List


class Solution:
    # dp
    def trap(self, height: List[int]) -> int:
        l = len(height)
        if l < 3:
            return 0

        # define and init
        lefts = [0] * (l)
        rights = [0] * (l)

        # loop lefts
        maxLeft = 0
        for i in range(l):
            maxLeft = max(maxLeft, height[i])
            lefts[i] = maxLeft

        # loop right:
        maxRight = 0
        for i in range(l - 1, -1, -1):
            maxRight = max(maxRight, height[i])
            rights[i] = maxRight

        res = 0
        # calculate
        for i in range(l):
            res += min(lefts[i], rights[i]) - height[i]

        return res

    # stack
    def trap2(self, height: List[int]) -> int:
        l = len(height)
        if l < 3:
            return 0
        res = 0
        stack = []
        for i, h in enumerate(height):
            while stack and height[stack[-1]] <= h:
                bottom_idx = stack.pop()
                if not stack:
                    break
                delta = min(height[stack[-1]], h) - height[bottom_idx]
                distance = i - stack[-1] - 1
                res += delta * distance
            stack.append(i)
        return res

    # double cursor
    def trap3(self, height: List[int]) -> int:
        l = len(height)
        if l < 3:
            return 0
        res = 0

        left, right = 0, l-1
        maxLeft = maxRight = 0

        while left < right:
            if height[left] < height[right]:
                maxLeft = max(maxLeft, height[left])
                res += maxLeft - height[left]
                left += 1
            else:
                maxRight = max(maxRight, height[right])
                res += maxRight - height[right]
                right -= 1

        return res


obj = Solution()
height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(obj.trap3(height))
