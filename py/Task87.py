# 给定一个字符串 s1，我们可以把它递归地分割成两个非空子字符串，从而将其表示为二叉树。

# 下图是字符串 s1 = "great" 的一种可能的表示形式。

#     great
#    /    \
#   gr    eat
#  / \    /  \
# g   r  e   at
#            / \
#           a   t
# 在扰乱这个字符串的过程中，我们可以挑选任何一个非叶节点，然后交换它的两个子节点。

# 例如，如果我们挑选非叶节点 "gr" ，交换它的两个子节点，将会产生扰乱字符串 "rgeat" 。

#     rgeat
#    /    \
#   rg    eat
#  / \    /  \
# r   g  e   at
#            / \
#           a   t
# 我们将 "rgeat” 称作 "great" 的一个扰乱字符串。

# 同样地，如果我们继续交换节点 "eat" 和 "at" 的子节点，将会产生另一个新的扰乱字符串 "rgtae" 。

#     rgtae
#    /    \
#   rg    tae
#  / \    /  \
# r   g  ta  e
#        / \
#       t   a
# 我们将 "rgtae” 称作 "great" 的一个扰乱字符串。

# 给出两个长度相等的字符串 s1 和 s2，判断 s2 是否是 s1 的扰乱字符串。

# 示例 1:

# 输入: s1 = "great", s2 = "rgeat"
# 输出: true
# 示例 2:

# 输入: s1 = "abcde", s2 = "caebd"
# 输出: false

from collections import Counter


class Solution:
    # recursion + 记忆化
    def isScramble(self, s1: str, s2: str) -> bool:
        map = {}

        def helper(s1: str, s2: str) -> bool:
            if s1 == s2:
                return True
            key = s1+','+s2
            if key in map:
                return map[key]
            if Counter(s1) != Counter(s2):
                map[key] = False
                return False
            l = len(s1)
            for i in range(1, l):
                if helper(s1[0:i], s2[0:i]) and helper(s1[i:], s2[i:]) \
                        or helper(s1[0:i], s2[l-i:]) and helper(s1[i:], s2[0:l-i]):
                    map[key] = True
                    return True
            return False
        return helper(s1, s2)

    # dp
    def isScramble2(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        if Counter(s1) != Counter(s2):
            return False
        l = len(s1)
        # define & init
        dp = [[[False] * l for _ in range(l)] for _ in range(l+1)]
        for ll in range(1, l+1):
            for i in range(l-ll+1):
                for j in range(l-ll+1):
                    if ll == 1:
                        dp[ll][i][j] = s1[i] == s2[j]
                    else:
                        for q in range(1, ll):
                            if dp[q][i][j] and dp[ll-q][i+q][j+q] or dp[q][i][j+ll-q] and dp[ll-q][i+q][j]:
                                dp[ll][i][j] = True
                                break
        return dp[l][0][0]
    # others

    def isScramble3(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        if sorted(s1) != sorted(s2):
            return False
        for i in range(1, len(s1)):
            if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]):
                return True
            if self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i]):
                return True
        return False


so = Solution()
s1 = "great"
s2 = "rgeat"
print(so.isScramble2(s1, s2))
