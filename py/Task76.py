from collections import Counter


class Solution:
    # slide window
    def minWindow(self, s: str, t: str) -> str:
        cs, ct = Counter(), Counter(t)
        left, right = 0, 0
        resLeft, resRight = -1, len(s)

        while right < len(s):
            cs[s[right]] += 1
            right += 1
            while not ct - cs:
                if right - left < resRight - resLeft:
                    resLeft, resRight = left, right
                cs[s[left]] -= 1
                left += 1

        if resLeft == -1:
            return ''
        return s[resLeft:resRight]

    # slide window 优化，不在比较两个字符串counter，改为使用一个
    def minWindow2(self, s: str, t: str) -> str:
        need = Counter(t)
        needCnt = len(t)
        left, right = 0, 0
        resLeft, resRight = -1, len(s)

        while right < len(s):
            cr = s[right]
            right += 1
            if cr in need:
                need[cr] -= 1
                if need[cr] >= 0:
                    needCnt -= 1
                while needCnt == 0:
                    if right - left < resRight - resLeft:
                        resLeft, resRight = left, right
                    cl = s[left]
                    if cl in need:
                        need[cl] += 1
                        if need[cl] > 0:
                            needCnt += 1
                    left += 1

        if resLeft == -1:
            return ''
        return s[resLeft:resRight]


S = "ADOBECODEBANC"
T = "ABC"
obj = Solution()
print(obj.minWindow2(S, T))
