class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        def dfs(n: int, k: int, s: str, canUse: set) -> None:
            if self.cnt == k:
                return
            if len(s) == n:
                self.cnt += 1
                if self.cnt == k:
                    self.res = s
                return
            for i in range(1, n+1):
                if i in canUse:
                    canUse.remove(i)
                    dfs(n, k, s+str(i), canUse)
                    canUse.add(i)

        self.cnt = 0
        canUse = {i for i in range(1, n+1)}
        dfs(n, k, '', canUse)
        return self.res

    def getPermutation2(self, n: int, k: int) -> str:
        used = [0 for _ in range(n+1)]
        factorial = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
        res = ''
        while len(res) != n:
            for i in range(1, n+1):
                if used[i]:
                    continue
                if factorial[n-len(res)-1] >= k:
                    res+=str(i)
                    used[i] = 1
                    break
                else:
                    k-=factorial[n-len(res)-1]
        return res


solution = Solution()
n = 4
k = 9
print(solution.getPermutation2(4, 9))
