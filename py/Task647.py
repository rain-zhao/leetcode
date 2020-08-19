class Solution:
    # 中心扩展
    def countSubString(self, s: str) -> int:
        if not s:
            return 0
        cnts = 0
        l = len(s)
        for i in range(l):
            # 以一个字母为中心拓展
            cnt = 0
            left, right = i, i
            while left >= 0 and right < l and s[left] == s[right]:
                cnt += 1
                left -= 1
                right += 1
            cnts += cnt
            # 以两个字母中间为中心拓展
            cnt = 0
            left, right = i, i+1
            while left >= 0 and right < l and s[left] == s[right]:
                cnt += 1
                left -= 1
                right += 1
            cnts += cnt
        return cnts

    # dp
    def countSubString2(self, s: str) -> int:
        if not s:
            return 0
        cnts = 0
        l = len(s)
        # define and init
        dp = [[False] * l for _ in range(l)]
        # init
        for i in range(l-1):
            dp[i][i] = True
            cnts += 1
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                cnts += 1
        dp[l-1][l-1] = True
        cnts += 1
        # dp iter
        for delta in range(2, l):
            for i in range(l - delta):
                j = i + delta
                if dp[i+1][j-1] and s[i] == s[j]:
                    dp[i][j] = True
                    cnts += 1
        return cnts

    # 中心扩展代码优化
    def countSubString3(self, s: str) -> int:
        cnts = 0
        l = len(s)
        for i in range(2 * l - 1):
            left, right = i >> 1, (i+1) >> 1
            while left >= 0 and right < l and s[left] == s[right]:
                cnts += 1
                left -= 1
                right += 1
        return cnts


s = "aaa"
obj = Solution()
print(obj.countSubString3(s))
