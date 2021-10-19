class Solution:
    def countAndSay(self, n: int) -> str:
        s = '1'
        for _ in range(n-1):
            pre = s[0]
            cnt = 1
            ss = ''
            for c in s[1:]:
                if pre == c:
                    cnt += 1
                else:
                    ss += str(cnt) + pre
                    pre = c
                    cnt = 1
            ss += str(cnt) + pre
            s = ss
        return s


n = 5
obj = Solution()
print(obj.countAndSay(n))
