from collections import defaultdict


class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        str = str.split()
        if len(pattern) != len(str):
            return False
        map1, map2 = {}, {}
        for i, j in zip(pattern, str):
            if i in map1 and map1[i] != j or j in map2 and map2[j] != i:
                return False
            map1[i] = j
            map2[j] = i
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
str = "dog cat cat fish"
so = Solution()
print(so.wordPattern(pattern, str))
