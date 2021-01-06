from typing import List


class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        k = 1
        res = []
        l = len(s)
        for i in range(1, l):
            if s[i] == s[i-1]:
                k += 1
            else:
                if k >= 3:
                    res.append([i-k, i-1])
                k = 1
        if k >= 3:
            res.append([l-k, l-1])
        return res


s = "abbxxxxzzy"
obj = Solution()
print(obj.largeGroupPositions(s))
