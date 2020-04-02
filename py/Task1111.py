from typing import List


class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        res = []
        cnt = 0
        for c in seq:
            if c == '(':
                cnt += 1
                res.append(0 if cnt & 1 else 1)
            else:
                cnt -= 1
                res.append(1 if cnt & 1 else 0)
        return res

    def maxDepthAfterSplit2(self, seq: str) -> List[int]:
        res = []
        for i, c in enumerate(seq):
            if c == '(':
                res.append(1 if i & 1 else 0)
            else:
                res.append(0 if i & 1 else 1)
        return res


seq = "(()())"
obj = Solution()
print(obj.maxDepthAfterSplit2(seq))
