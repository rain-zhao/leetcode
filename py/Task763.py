from typing import List


class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        # pre-process
        lastOccur = {}
        for idx, c in enumerate(S):
            lastOccur[c] = idx
        res = []
        beg = end = -1
        # loop
        for idx, c in enumerate(S):
            end = max(end, lastOccur[c])
            if idx == end:
                res.append(end-beg)
                beg = idx
        return res


S = "ababcbacadefegdehijhklij"
obj = Solution()
print(obj.partitionLabels(S))
