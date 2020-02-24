from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(s):
            left, right = 0, len(s)-1
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
        if not s:
            return [[]]
        res = []
        for i in range(len(s)-1, -1, -1):
            subStr = s[i:]
            if isPalindrome(subStr):
                candidates = self.partition(s[:i])
                res += [v + [subStr] for v in candidates]
        return res
    def partition2(self, s: str) -> List[List[str]]:
        if not s:
            return [[]]
        l = len(s)
        dp = [[False]*l for _ in range(l)]
        for j in range(l):
            for i in range(j+1):
                if s[i] == s[j] and (j-i < 2 or dp[i+1][j-1]):
                    dp[i][j] = True
        res = []

        def helper(i,list):
            if i == l:
                res.append(list)
            for j in range(i,l):
                if dp[i][j]:
                    helper(j+1,list+[s[i:j+1]])
        helper(0,[])
        return res
    # 在已有的字符串基础上增加一个字母，除了在每个结果后面加上新字母外，
    # 增加的字母还有可能与前结果的最后一个回文，或者最后两个回文组成新回文，没有其他情况。
    def partition3(self, s: str) -> List[List[str]]:
        if not s:
            return [[]]
        l = len(s)
        res = [[]]
        for i in range(l):
            for p in res[:len(res)]:
                if len(p) >= 2 and p[-2] == s[i]:
                    res.append(p[:-2]+[p[-2]+p[-1]+s[i]])
                if len(p) >= 1 and p[-1] == s[i]:
                    res.append(p[:-1]+[p[-1]+s[i]])
                p.append(s[i])
        return res


so = Solution()
s =  "aab"
print(so.partition3(s))