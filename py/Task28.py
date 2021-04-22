from typing import List


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)

    # KMP
    def strStr2(self, haystack: str, needle: str) -> int:
        def genNext(s: str) -> List[int]:
            n = len(s)
            next = [-1] * n
            j = -1
            for i in range(n-1):
                while j != -1 and s[i] != s[j]:
                    j = next[j]
                j += 1
                next[i+1] = j
            return next
        next = genNext(needle)
        m, n = len(haystack), len(needle)
        i = j = 0
        while i < m and j < n:
            if j == -1 or haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                j = next[j]
        return -1 if j != n else i - n


haystack = "mississippi"
needle = "issip"
obj = Solution()
print(obj.strStr2(haystack, needle))
