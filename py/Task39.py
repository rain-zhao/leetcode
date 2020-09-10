# 给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

# candidates 中的数字可以无限制重复被选取。

# 说明：

# 所有数字（包括 target）都是正整数。
# 解集不能包含重复的组合。
# 示例 1:

# 输入: candidates = [2,3,6,7], target = 7,
# 所求解集为:
# [
#   [7],
#   [2,2,3]
# ]
# 示例 2:

# 输入: candidates = [2,3,5], target = 8,
# 所求解集为:
# [
#   [2,2,2,2],
#   [2,3,3],
#   [3,5]
# ]
from typing import List


class Solution:
    # dfs
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res = []
        l = len(candidates)
        if not candidates:
            return self.res

        def _dfs(idx: int, target, subList: List[int]):
            # terminate
            if target == 0:
                self.res += [subList]
                return
            if target < 0:
                return
            # process
            # drill down
            for i in range(idx, l):
                _dfs(i, target-candidates[i], subList+[candidates[i]])

        _dfs(0, target, [])
        return self.res

    # 2020-09-09 dfs
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(candidates)

        def dfs(i: int, remain: int, l: List[int]):
            if remain == 0:
                res.append(l)
                return
            if i == n or remain < 0:
                return
            # not choose
            dfs(i+1, remain, l)
            # choose
            dfs(i, remain - candidates[i], l+[candidates[i]])
        dfs(0, target, [])
        return res


obj = Solution()
candidates = [2, 3, 5]
target = 8
print(obj.combinationSum2(candidates, target))
