from typing import List


class KMPMatch:
    def match(self, s: str, p: str) -> bool:
        next = self.genNext(p)
        m, n = len(s), len(p)
        i = j = 0
        while i < m and j < n:
            if j == -1 or s[i] == p[j]:
                i += 1
                j += 1
            else:
                j = next[j]
        return j == n

    def genNext(self, s: str) -> List[int]:
        n = len(s)
        next = [-1] * n
        j = -1
        for i in range(n-1):
            while j != -1 and s[i] != s[j]:
                j = next[j]
            j += 1
            next[i + 1] = j
        return next


s = 'helloworld'
p = 'hello'
obj = KMPMatch()
print(obj.match(s, p))
