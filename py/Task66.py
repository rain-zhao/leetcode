from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        for idx in range(n-1, -1, -1):
            if digits[idx] != 9:
                digits[idx] += 1
                break
            digits[idx] = 0
        if not digits[0]:
            digits = [1] + digits
        return digits


digits = [9, 9, 9, 9]
obj = Solution()
print(obj.plusOne(digits))
