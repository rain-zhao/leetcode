from collections import Counter


class Solution:
    def sortString(self, s: str) -> str:
        counter = Counter(s)
        items = sorted(counter)
        res = ''
        while items:
            for c in items[:]:
                res += c
                counter[c] -= 1
                if counter[c] == 0:
                    items.remove(c)
            for c in items[::-1]:
                res += c
                counter[c] -= 1
                if counter[c] == 0:
                    items.remove(c)
        return res


s = "aaaabbbbcccc"
obj = Solution()
print(obj.sortString(s))
