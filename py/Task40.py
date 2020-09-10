from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(candidates)
        candidates.sort()

        def dfs(i: int, target: int, l: List[int]):
            if target == 0:
                res.append(l)
                return
            if i == n or target < 0:
                return
            # not choose
            j = i+1
            while j < n and candidates[i] == candidates[j]:
                j += 1
            dfs(j, target, l)
            # choose
            dfs(i+1, target - candidates[i], l + [candidates[i]])
        dfs(0, target, [])
        return res


candidates = [2, 5, 2, 1, 2]
target = 5
obj = Solution()
print(obj.combinationSum2(candidates, target))
