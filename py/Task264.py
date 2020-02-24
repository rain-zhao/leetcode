class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n == 1:
            return 1
        set = {1}
        cur = 2
        while True:
            for i in (2, 3, 5):
                if cur % i == 0 and cur // i in set:
                    if len(set) == n-1:
                        return cur
                    set.add(cur)
                    break
            cur += 1
        return None

    def nthUglyNumber2(self, n: int) -> int:
        dp = [0] * n
        dp[0] = 1
        l2 = l3 = l5 = 0
        for i in range(1, n):
            dp[i] = min(2*dp[l2], 3*dp[l3], 5*dp[l5])
            if dp[i] == 2*dp[l2]:
                l2 += 1
            if dp[i] == 3*dp[l3]:
                l3 += 1
            if dp[i] == 5*dp[l5]:
                l5 += 1
        return dp[-1]


so = Solution()
n = 10
print(so.nthUglyNumber2(n))
