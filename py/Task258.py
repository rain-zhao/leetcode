from functools import reduce


class Solution:
    def addDigits(self, num: int) -> int:
        if num < 10:
            return num
        return self.addDigits(reduce(lambda x, y: int(x)+int(y), list(str(num))))

    def addDigits2(self, num: int) -> int:
        while len(str(num)) > 1:
            num = eval('+'.join(str(num)))
        return num

    def addDigits3(self, num: int) -> int:
        if num < 10:
            return num
        num %=9
        return num if num != 0 else 9


num = 123
so = Solution()
print(so.addDigits2(num))
