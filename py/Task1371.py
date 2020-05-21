class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        lens = [-1] * 32
        lens[0] = 0
        b = 0
        res = 0
        for i, c in enumerate(s):
            if c == 'a':
                b ^= 1
            elif c == 'e':
                b ^= 2
            elif c == 'i':
                b ^= 4
            elif c == 'o':
                b ^= 8
            elif c == 'u':
                b ^= 16
            if lens[b] != -1:
                res = max(res, i + 1 - lens[b])
            else:
                lens[b] = i + 1

        return res


s = "eleetminicoworoep"
obj = Solution()
print(obj.findTheLongestSubstring(s))
