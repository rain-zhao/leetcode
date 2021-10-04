class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        # rm '-' from s
        s = s.replace('-', '').upper()
        l = len(s)
        if l == 0:
            return ''
        # calc total segment(-1) count & first segment' size
        m, n = l//k, l % k
        # define output & second segment cursor
        res, cur = '', n
        # first segment
        res += s[0:n]
        # remain segments
        for _ in range(m):
            res += '-' + s[cur:cur+k]
            cur += k
        # return
        return res[1:] if res[0] == '-' else res

    def licenseKeyFormatting2(self, s: str, k: int) -> str:
        s = s.replace('-', '').upper()[::-1]
        segments = [s[i:i+k] for i in range(0, len(s), k)]
        return '-'.join(segments)[::-1]


obj = Solution()
S = "2-5g-3-J"
K = 2
print(obj.licenseKeyFormatting2(S, K))
