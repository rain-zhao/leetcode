from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        appear = set()
        res = set()
        for i in range(len(s)-9):
            ss = s[i:i+10]
            if ss in appear:
                res.add(ss)
            else:
                appear.add(ss)
        return list(res)
