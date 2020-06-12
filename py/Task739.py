class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        res = [0] * len(T)
        stack = []
        for idx, num in enumerate(T):
            while stack and T[stack[-1]] < num:
                popIdx = stack.pop()
                res[popIdx] = idx - popIdx
            stack.append(idx)
        return res
