from collections import deque
from functools import cache, reduce
from tokenize import TokenInfo
from typing import Counter, List


class Solution:
    # bfs
    def minStickers(self, stickers: List[str], target: str) -> int:
        # targer counter
        tc = Counter(target)
        # stickers counter
        scs = [Counter(sticker) for sticker in stickers]

        if len(set(tc) - reduce(lambda x, y: x | set(y), stickers, set())) > 0:
            return -1

        ret = 0
        dq = deque([tc])

        while dq:
            ret += 1
            size = len(dq)
            for _ in range(size):
                # current tc
                curtc = dq.popleft()
                for sc in scs:
                    # remain tc
                    rtc = curtc - sc
                    if len(rtc) == 0:
                        return ret
                    dq.append(rtc)

        return -1

    # dfs + memory
    def minStickers2(self, stickers: List[str], target: str) -> int:
        l = len(target)

        @cache
        def dfs(mask):
            if mask == 0:
                return 0
            res = l + 1
            for sticker in stickers:
                left = mask
                sc = Counter(sticker)

                for i, c in enumerate(target):
                    if left & 1 << i and sc[c]:
                        sc[c] -= 1
                        left ^= 1 << i

                if left < mask:
                    res = min(res, dfs(left)+1)
            return res

        res = dfs((1 << l) - 1)
        return res if res <= len(target) else -1


stickers = ["with", "example", "science"]
target = "thehat"
obj = Solution()
print(obj.minStickers2(stickers, target))
