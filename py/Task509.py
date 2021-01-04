class Solution:
    # recusrsion
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        return self.fib(n-1)+self.fib(n-2)

    # dp
    def fib2(self, n: int) -> int:
        if n < 2:
            return n
        p0, p1 = 0, 1
        for _ in range(2, n+1):
            p0, p1 = p1, p0+p1
        return p1


n = 4
obj = Solution()
print(obj.fib(n))
