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


obstacleGrid = [
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
solution = Solution()
print(solution.uniquePathsWithObstacles(obstacleGrid))

