class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: [[int]]) -> int:
        if not len(obstacleGrid) or not len(obstacleGrid[0]):
            return 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [0 for _ in range(n+1)]
        dp[1] = 1

        for i in range(m):
            for j in range(n):
                dp[j+1] = 0 if obstacleGrid[i][j] else dp[j]+dp[j+1]

        return dp[n]

    # dp 2020-07-06
    def uniquePathsWithObstacles2(self, obstacleGrid: [[int]]) -> int:
        if not obstacleGrid or not obstacleGrid[0] or obstacleGrid[0][0]:
            return 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        # define
        dp = [[0] * n for _ in range(m)]

        # init
        dp[0][0] = 1
        for i in range(1, m):
            dp[i][0] = dp[i - 1][0] if not obstacleGrid[i][0] else 0
        for i in range(1, n):
            dp[0][i] = dp[0][i - 1] if not obstacleGrid[0][i] else 0

        # loop
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i][j - 1] + \
                    dp[i - 1][j] if not obstacleGrid[i][j] else 0
        return dp[-1][-1]

    # dp 压缩空间2020-07-06
    def uniquePathsWithObstacles3(self, obstacleGrid: [[int]]) -> int:
        if not obstacleGrid or not obstacleGrid[0] or obstacleGrid[0][0]:
            return 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        # define
        dp = [0] * (n + 1)
        dp[1] = 1

        for i in range(m):
            for j in range(n):
                dp[j + 1] = dp[j + 1] + dp[j] if not obstacleGrid[i][j] else 0
        return dp[-1]


obstacleGrid = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
]
solution = Solution()
print(solution.uniquePathsWithObstacles3(obstacleGrid))
