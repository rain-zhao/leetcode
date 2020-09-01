# 给定一个表示分数的非负整数数组。 玩家 1 从数组任意一端拿取一个分数，随后玩家 2 继续从剩余数组任意一端拿取分数，然后玩家 1 拿，…… 。每次一个玩家只能拿取一个分数，分数被拿取之后不再可取。直到没有剩余分数可取时游戏结束。最终获得分数总和最多的玩家获胜。

# 给定一个表示分数的数组，预测玩家1是否会成为赢家。你可以假设每个玩家的玩法都会使他的分数最大化。

#  

# 示例 1：

# 输入：[1, 5, 2]
# 输出：False
# 解释：一开始，玩家1可以从1和2中进行选择。
# 如果他选择 2（或者 1 ），那么玩家 2 可以从 1（或者 2 ）和 5 中进行选择。如果玩家 2 选择了 5 ，那么玩家 1 则只剩下 1（或者 2 ）可选。
# 所以，玩家 1 的最终分数为 1 + 2 = 3，而玩家 2 为 5 。
# 因此，玩家 1 永远不会成为赢家，返回 False 。
# 示例 2：

# 输入：[1, 5, 233, 7]
# 输出：True
# 解释：玩家 1 一开始选择 1 。然后玩家 2 必须从 5 和 7 中进行选择。无论玩家 2 选择了哪个，玩家 1 都可以选择 233 。
#      最终，玩家 1（234 分）比玩家 2（12 分）获得更多的分数，所以返回 True，表示玩家 1 可以成为赢家。
#  

# 提示：

# 1 <= 给定的数组长度 <= 20.
# 数组里所有分数都为非负数且不会大于 10000000 。
# 如果最终两个玩家的分数相等，那么玩家 1 仍为赢家。


from typing import List


class Solution:
    # dp
    def PredictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        # define
        dp = [[[0, 0] for _ in range(n)] for _ in range(n)]
        # init
        for i in range(n):
            dp[i][i][0] = nums[i]
        # loop
        for k in range(1, n):
            for i in range(0, n - k):
                j = i + k
                if dp[i + 1][j][0] > dp[i][j-1][0]:
                    dp[i][j][0] = dp[i][j-1][1] + nums[j]
                    dp[i][j][1] = dp[i][j-1][0]
                else:
                    dp[i][j][0] = dp[i+1][j][1] + nums[i]
                    dp[i][j][1] = dp[i+1][j][0]
        return dp[0][-1][0] - dp[0][-1][1] >= 0

    # brute-force 记录分差
    def PredictTheWinner2(self, nums: List[int]) -> bool:
        n = len(nums)

        def dfs(beg: int, end: int, turn: int) -> int:
            if beg == end:
                return nums[beg] * turn
            startScore = nums[beg] * turn + dfs(beg+1, end, -turn)
            endScore = nums[end] * turn + dfs(beg, end-1, -turn)
            return max(startScore, endScore) if turn == 1 else min(startScore, endScore)
        return dfs(0, n-1, 1) >= 0

    # brute-force 记录分差
    def PredictTheWinner3(self, nums: List[int]) -> bool:
        n = len(nums)

        def dfs(beg: int, end: int) -> int:
            if beg == end:
                return nums[beg]
            startScore = nums[beg] - dfs(beg+1, end)
            endScore = nums[end] - dfs(beg, end-1)
            return max(startScore, endScore)
        return dfs(0, n-1) >= 0

    # dp 记录分差
    def PredictTheWinner4(self, nums: List[int]) -> bool:
        n = len(nums)
        # define
        dp = [[0] * n for _ in range(n)]
        # init
        for i in range(n):
            dp[i][i] = nums[i]
        for k in range(1, n):
            for i in range(0, n - k):
                j = i + k
                begScore = nums[i] - dp[i + 1][j]
                endScore = nums[j] - dp[i][j - 1]
                dp[i][j] = max(begScore, endScore)
        return dp[0][n-1] >= 0

    # dp 记录分差 空间压缩
    def PredictTheWinner5(self, nums: List[int]) -> bool:
        n = len(nums)
        # define & init
        dp = nums[:]
        for i in range(n-2, -1, -1):
            for j in range(i+1, n):
                dp[j] = max(nums[i] - dp[j], nums[j] - dp[j-1])
        return dp[-1] >= 0


nums = [1, 5, 2]
obj = Solution()
print(obj.PredictTheWinner5(nums))
