from typing import List


class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        dp = [1] * n
        pos = [0] * len(primes)
        for i in range(1, n):
            dp[i] = min((dp[j] * k for j, k in zip(pos, primes)))
            for idx in range(len(primes)):
                if dp[i] == dp[pos[idx]] * primes[idx]:
                    pos[idx] += 1
        return dp[-1]


n = 12
primes = [2, 7, 13, 19]
so = Solution()
print(so.nthSuperUglyNumber(n, primes))
