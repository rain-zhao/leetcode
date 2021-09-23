class Solution:
    # recursion
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1:
            return True
        if n == 0 or n % 3:
            return False
        return self.isPowerOfThree(n//3)

    #  using iteration
    def isPowerOfThree2(self, n: int) -> bool:
        if n <= 0:
            return False
        while not n % 3:
            n //= 3
        return n == 1

    def isPowerOfThree3(self, n: int) -> bool:
        return n > 0 and not 3**19 % n
