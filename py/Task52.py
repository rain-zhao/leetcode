class Solution:
    def totalNQueens(self, n: int) -> int:
        self.res = 0
        mask = (1 << n)-1

        def dfs(idx: int, C: int, P: int, N: int):
            if idx == n:
                self.res += 1
                return
            # avaliable
            avals = mask & ~(C | P | N)
            # iter
            while avals:
                aval = avals & -avals
                dfs(idx+1, C | aval, (P | aval) << 1, (N | aval) >> 1)
                avals = avals & avals-1
        dfs(0, 0, 0, 0)
        return self.res


n = 4
obj = Solution()
print(obj.totalNQueens(n))
