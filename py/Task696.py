# 给定一个字符串 s，计算具有相同数量0和1的非空(连续)子字符串的数量，并且这些子字符串中的所有0和所有1都是组合在一起的。

# 重复出现的子串要计算它们出现的次数。

# 示例 1 :

# 输入: "00110011"
# 输出: 6
# 解释: 有6个子串具有相同数量的连续1和0：“0011”，“01”，“1100”，“10”，“0011” 和 “01”。

# 请注意，一些重复出现的子串要计算它们出现的次数。

# 另外，“00110011”不是有效的子串，因为所有的0（和1）没有组合在一起。
# 示例 2 :

# 输入: "10101"
# 输出: 4
# 解释: 有4个子串：“10”，“01”，“10”，“01”，它们具有相同数量的连续1和0。
# 注意：

# s.length 在1到50,000之间。
# s 只包含“0”或“1”字符。


class Solution:
    # 记录前缀有多少个相同的元素
    def countBinarySubstrings(self, s: str) -> int:
        l = len(s)
        pre = [0, 1]
        res = 0
        for i in range(1, l):
            if s[i] != s[i-1]:
                pre.append(1)
                res += 1
            else:
                pre[-1] += 1
                if pre[-1] <= pre[-2]:
                    res += 1
        return res

    # dp + 压缩：dp[i] 已第i字符结尾的符合要求的字串长度
    def countBinarySubstrings2(self, s: str) -> int:
        l = len(s)
        pre = 0
        res = 0
        for i in range(1, l):
            if s[i] != s[i-1]:
                pre = 2
                res += 1
            elif (beg:=i-pre-1) >= 0 and s[i] != s[beg]:
                pre += 2
                res += 1
            else:
                pre = 0
        return res

    # 先合并连续出现的字串，再计算相邻的数字
    def countBinarySubstrings3(self, s: str) -> int:
        counts = []
        count = 1
        for c1, c2 in zip(s, s[1:]):
            if c1 == c2:
                count += 1
            else:
                counts.append(count)
                count = 1
        counts.append(count)
        res = 0
        for c1, c2 in zip(counts, counts[1:]):
            res += min(c1, c2)
        return res

    def countBinarySubstrings4(self, s: str) -> int:
        pre, cur = 0, 1
        res = 0
        for c1, c2 in zip(s, s[1:]):
            if c1 == c2:
                cur += 1
            else:
                res += min(pre, cur)
                pre, cur = cur, 1
        res += min(pre, cur)
        return res


obj = Solution()
s = "00110011"
print(obj.countBinarySubstrings4(s))
