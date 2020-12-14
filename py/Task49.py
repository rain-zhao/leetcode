from typing import List
from collections import defaultdict
from collections import Counter


class Solution:
    # sort O(nklogk)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            res[''.join(sorted(s))].append(s)
        return list(res.values())

    # hash or counter
    def groupAnagrams2(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            counter = [0] * 26
            for c in s:
                counter[ord(c) - 97] += 1
            key = ''.join(str(i) for i in counter)
            res[key].append(s)
        return list(res.values())

    # hash or counter
    def groupAnagrams3(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            a, b = 1, 0
            for c in s:
                a *= ord(c)
                b += ord(c)
            key = a + b
            res[key].append(s)
        return list(res.values())


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
obj = Solution()
print(obj.groupAnagrams3(strs))
