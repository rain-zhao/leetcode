from typing import List


class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        res = []
        mask = 1 << label.bit_length()-1
        while label != 1:
            res.append(label)
            mask >>= 1
            label = label >> 1 ^ mask-1
        return [1]+res[::-1]


label = 1
so = Solution()
print(so.pathInZigZagTree(label))
