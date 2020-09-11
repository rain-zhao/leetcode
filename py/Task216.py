from typing import List, Set


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []

        def dfs(k: int, n: int, idx: int, candidate: List[int]):
            if n == 0 or k == 0 or idx == 10:
                if n == 0 and k == 0:
                    res.append(candidate[:])
                return
            for i in range(idx, min(10, n+1)):
                candidate.append(i)
                dfs(k-1, n-i, i+1, candidate)
                candidate.pop()
        dfs(k, n, 1, [])
        return res

    # dfs:optimize code,no using for loop
    def combinationSum32(self, k: int, n: int) -> List[List[int]]:
        res = []

        def dfs(num: int, n: int, candidate: List[int]):
            if len(candidate) == k:
                if n == 0:
                    res.append(candidate)
                return
            if num > 9 or n < 0:
                return
            # not choose
            dfs(num+1, n, candidate)
            # choose
            dfs(num+1, n-num, candidate + [num])
        dfs(1, n, [])
        return res


k = 3
n = 9
so = Solution()
print(so.combinationSum3(k, n))
