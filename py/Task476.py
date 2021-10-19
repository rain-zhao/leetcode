class Solution:
    def findComplement(self, num: int) -> int:
        tmp, mask = num, 1
        while tmp:
            mask <<= 1
            tmp >>= 1
        mask -= 1
        return num ^ mask


obj = Solution()
num = 5
print(obj.findComplement(num))
