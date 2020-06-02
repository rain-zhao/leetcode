class Solution:
    def sumNums(self, n: int) -> int:
        return (n**2+n) >> 1

    def sumNums2(self, n: int) -> int:
        self.res = 0

        def dfs(n: int):
            n and dfs(n-1)
            self.res += n
        dfs(n)
        return self.res


n = 3
obj = Solution()
print(obj.sumNums2(n))
