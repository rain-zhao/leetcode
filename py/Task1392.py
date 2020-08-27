# 「快乐前缀」是在原字符串中既是 非空 前缀也是后缀（不包括原字符串自身）的字符串。

# 给你一个字符串 s，请你返回它的 最长快乐前缀。

# 如果不存在满足题意的前缀，则返回一个空字符串。

#  

# 示例 1：

# 输入：s = "level"
# 输出："l"
# 解释：不包括 s 自己，一共有 4 个前缀（"l", "le", "lev", "leve"）和 4 个后缀（"l", "el", "vel", "evel"）。最长的既是前缀也是后缀的字符串是 "l" 。
# 示例 2：

# 输入：s = "ababab"
# 输出："abab"
# 解释："abab" 是最长的既是前缀也是后缀的字符串。题目允许前后缀在原字符串中重叠。
# 示例 3：

# 输入：s = "leetcodeleet"
# 输出："leet"
# 示例 4：

# 输入：s = "a"
# 输出：""
#  

# 提示：

# 1 <= s.length <= 10^5
# s 只含有小写英文字母


class Solution:
    # brute-force
    def longestPrefix(self, s: str) -> str:
        n = len(s)
        for p in range(n-1, 0, -1):
            if s[:p] == s[-p:]:
                return s[:p]
        return ''

    # Rabin-Karp
    def longestPrefix2(self, s: str) -> str:
        n = len(s)
        res = 0
        prefix = suffix = 0
        base, mod, mul = 31, 1000000007, 1
        for i in range(1, n):
            prefix = (prefix * base + ord(s[i-1]) - 97) % mod
            suffix = (suffix + (ord(s[-i]) - 97) * mul) % mod
            if prefix == suffix:
                res = i
            mul = mul * base % mod
        return s[:res]

    # KMP / dp
    def longestPrefix3(self, s: str) -> str:
        n = len(s)
        next = [-1] * (n + 1)
        j = -1
        for i in range(n):
            while j != -1 and s[i] != s[j]:
                j = next[j]
            j += 1
            next[i + 1] = j
        return s[:next[-1]]


s = "level"
obj = Solution()
print(obj.longestPrefix3(s))
