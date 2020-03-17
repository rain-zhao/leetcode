# 给定一个字符串数组 words，找到 length(word[i]) * length(word[j]) 的最大值，并且这两个单词不含有公共字母。你可以认为每个单词只包含小写字母。如果不存在这样的两个单词，返回 0。

# 示例 1:

# 输入: ["abcw","baz","foo","bar","xtfn","abcdef"]
# 输出: 16
# 解释: 这两个单词为 "abcw", "xtfn"。
# 示例 2:

# 输入: ["a","ab","abc","d","cd","bcd","abcd"]
# 输出: 4
# 解释: 这两个单词为 "ab", "cd"。
# 示例 3:

# 输入: ["a","aa","aaa","aaaa"]
# 输出: 0
# 解释: 不存在这样的两个单词。
from typing import List


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        # pre process
        map = {}
        for word in words:
            mask = 0
            for w in word:
                mask |= 1 << ord(w)-97
            map[mask] = max(len(word), map[mask] if mask in map else 0)
        res = 0
        # iter
        for x in map:
            for y in map:
                if x & y == 0:
                    res = max(map[x] * map[y], res)
        return res


obj = Solution()
words = ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
print(obj.maxProduct(words))
