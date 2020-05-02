# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

# 示例 1:

# 输入: "abcabcbb"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
# 示例 2:

# 输入: "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
# 示例 3:

# 输入: "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
#      请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。


class Solution:
    # dp 已压缩空间
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        map = {}
        res = cur = 0
        for idx, c in enumerate(s):
            cur = min(cur + 1, idx - map.get(c, -1))
            map[c] = idx
            res = max(cur, res)
        return res

    # dp 压缩空间 数组代替dict
    def lengthOfLongestSubstring2(self, s: str) -> int:
        if not s:
            return 0
        map = [-1] * 128
        res = cur = 0
        for idx, c in enumerate(s):
            cur = min(cur + 1, idx - map[ord(c)])
            map[ord(c)] = idx
            res = max(cur, res)
        return res

    # slide window
    def lengthOfLongestSubstring3(self, s: str) -> int:
        if not s:
            return 0
        map = {}
        res = 0
        left = right = -1
        for c in s:
            right += 1
            left = max(left, map.get(c, -1))
            map[c] = right
            res = max(res, right-left)
        return res


s = "abcabcbb"
obj = Solution()
print(obj.lengthOfLongestSubstring3(s))
