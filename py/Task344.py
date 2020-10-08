from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        s.reverse()

    # 左右指针
    def reverseString2(self, s: List[str]) -> None:
        left, right = 0, len(s)-1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
