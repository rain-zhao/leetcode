# 给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。

#  

# 示例：

# 输入："Let's take LeetCode contest"
# 输出："s'teL ekat edoCteeL tsetnoc"
#  

# 提示：

# 在字符串中，每个单词由单个空格分隔，并且字符串中不会有任何额外的空格。


class Solution:
    # split 再 reverse
    def reverseWords(self, s: str) -> str:
        if not s:
            return s
        array = s.split()
        res = ''
        for subStr in array:
            res += subStr[::-1] + ' '
        return res[:-1]

    # 一次遍历
    def reverseWords2(self, s: str) -> str:
        prev = 0
        res = ''
        for i in range(len(s)):
            if s[i] == ' ':
                res += s[prev:i][::-1] + ' '
                prev = i + 1
        res += s[prev:][::-1]
        return res

    # 使用数组递推式
    def reverseWords3(self, s: str) -> str:
        return ' '.join(c[::-1] for c in s.split())


s = "Let's take LeetCode contest"
obj = Solution()
print(obj.reverseWords3(s))
