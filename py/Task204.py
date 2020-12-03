
class Solution:
    def countPrimes(self, n: int) -> int:
        prime = [True] * n
        res = 0
        for i in range(2, n):
            if prime[i]:
                res += 1
                j = 2
                while i * j < n:
                    prime[i * j] = False
                    j += 1
        return res


n = 10
obj = Solution()
print(obj.countPrimes(n))
