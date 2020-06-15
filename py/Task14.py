# 编写一个函数来查找字符串数组中的最长公共前缀。

# 如果不存在公共前缀，返回空字符串 ""。

# 示例 1:

# 输入: ["flower","flow","flight"]
# 输出: "fl"
# 示例 2:

# 输入: ["dog","racecar","car"]
# 输出: ""
# 解释: 输入不存在公共前缀。
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ''
        for itms in zip(*strs):
            if list(itms) == [itms[0]] * len(itms):
                res += itms[0]
            else:
                break
        return res

    def longestCommonPrefix2(self, strs: List[str]) -> str:
        res = ''
        for itms in zip(*strs):
            if len(set(itms)) == 1:
                res += itms[0]
            else:
                break
        return res


obj = Solution()
strs = ["flower", "flow", "flight"]
obj.longestCommonPrefix(strs)
