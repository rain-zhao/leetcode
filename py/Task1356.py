from typing import List


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def bitcount(i: int) -> int:
            i = i - ((i >> 1) & 0x5555)
            i = (i & 0x3333) + ((i >> 2) & 0x3333)
            i = (i + (i >> 4)) & 0x0f0f
            i = i + (i >> 8)
            return i & 0x1f
        return sorted(arr, key=lambda x: (bitcount(x), x))


arr = [0, 1, 2, 3, 4, 5, 6, 7, 8]
obj = Solution()
print(obj.sortByBits(arr))
