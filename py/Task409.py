# 给定一个包含大写字母和小写字母的字符串，找到通过这些字母构造成的最长的回文串。

# 在构造过程中，请注意区分大小写。比如 "Aa" 不能当做一个回文字符串。

# 注意:
# 假设字符串的长度不会超过 1010。

# 示例 1:

# 输入:
# "abccccdd"

# 输出:
# 7

# 解释:
# 我们可以构造的最长的回文串是"dccaccd", 它的长度是 7。


class Solution:
    # using set
    def longestPalindrome(self, s: str) -> int:
        charset = set()
        res = 0
        for w in s:
            if w in charset:
                charset.remove(w)
                res += 2
            else:
                charset.add(w)
        if charset:
            res += 1
        return res

    # 位运算
    def longestPalindrome2(self, s: str) -> int:
        res = bits = 0
        for w in s:
            mask = 1 << ord(w)
            if bits & mask:
                bits ^= mask
                res += 2
            else:
                bits |= mask
        return res+1 if bits else res


obj = Solution()
s = "abccccdd"
print(obj.longestPalindrome2(s))
