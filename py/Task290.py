from collections import defaultdict


class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        str = str.split()
        if len(pattern) != len(str):
            return False
        map1 = {}
        map2 = {}
        for i, j in zip(pattern, str):
            if i not in map1 and j not in map2:
                map1[i] = j
                map2[j] = i
            elif i not in map1 or j not in map2 or map1[i] != j or map2[j] != i:
                return False
        return True

    def wordPattern2(self, pattern: str, str: str) -> bool:
        arr = str.split()
        if len(pattern) != len(arr):
            return False
        mp, s = {}, set()
        for p, word in zip(pattern, arr):
            if p in mp and mp[p] != word or p not in mp and word in s:
                return False
            mp[p] = word
            s.add(word)
        return True


pattern = "abba"
str = "dog cat cat dog"
so = Solution()
print(so.wordPattern2(pattern, str))
