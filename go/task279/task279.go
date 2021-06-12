package task279

// dp
func numSquares(n int) int {
	// define
	dp := make([]int, n+1)
	// init
	for i := 0; i <= n; i++ {
		dp[i] = i
	}
	candidates := []int{}
	for i := 1; i*i <= n; i++ {
		candidates = append(candidates, i*i)
	}
	for _, candidate := range candidates {
		for i := candidate; i <= n; i++ {
			if dp[i] > dp[i-candidate]+1 {
				dp[i] = dp[i-candidate] + 1
			}
		}
	}
	return dp[n]
}
