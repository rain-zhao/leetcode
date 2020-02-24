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


pattern = "abba"
str = "dog cat cat dog"
so = Solution()
print(so.wordPattern(pattern, str))
