# 给定一个字符串 s，你可以通过在字符串前面添加字符将其转换为回文串。找到并返回可以用这种方式转换的最短回文串。

# 示例 1:

# 输入: "aacecaaa"
# 输出: "aaacecaaa"
# 示例 2:

# 输入: "abcd"
# 输出: "dcbabcd"

from typing import List


class Solution:
    # KMP
    def shortestPalindrome(self, s: str) -> str:
        t = s[::-1]
        n = len(s)
        next = self.genNext(s)
        i = j = 0
        while i < n and j < n:
            if j == -1 or t[i] == s[j]:
                i += 1
                j += 1
            else:
                j = next[j]
        return t + s[j:]

    def genNext(self, s: str) -> List[int]:
        n = len(s)
        next = [-1] * n
        j = -1
        for i in range(n - 1):
            while j != -1 and s[i] != s[j]:
                j = next[j]
            j += 1
            next[i + 1] = j
        return next


s = "aacecaaa"
obj = Solution()
print(obj.shortestPalindrome(s))
