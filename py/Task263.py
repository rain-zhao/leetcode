class Solution:
    def isUgly(self, num: int) -> bool:
        if num <= 0:
            return False
        if num == 1:
            return True
        if not num % 2:
            return self.isUgly(num / 2)
        if not num % 3:
            return self.isUgly(num / 3)
        if not num % 5:
            return self.isUgly(num / 5)
        return False

    def isUgly2(self, num: int) -> bool:
        if num <= 0:
            return False
        while True:
            if num == 1:
                return True
            if not num % 2:
                num //= 2
                continue
            if not num % 3:
                num //= 3
                continue
            if not num % 5:
                num //= 5
                continue
            return False
        return False


obj = Solution()
num = 6
print(obj.isUgly(num))
