from collections import Counter


class Solution:
    # using hash (counter)
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

    # using array
    def isAnagram2(self, s: str, t: str) -> bool:
        m, n = len(s), len(t)
        if m != n:
            return False
        arr1, arr2 = [0] * 123, [0] * 123
        for i in range(m):
            arr1[ord(s[i])] += 1
            arr2[ord(t[i])] += 1
        return arr1 == arr2


s = "anagram"
t = "nagaram"
obj = Solution()
print(obj.isAnagram2(s, t))
