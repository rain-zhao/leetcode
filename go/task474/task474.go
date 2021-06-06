package task474

import (
	"strings"
)

// dp
func findMaxForm(strs []string, m int, n int) int {
	dp := make([][]int, n+1)
	for i := 0; i <= n; i++ {
		dp[i] = make([]int, m+1)
	}

	for _, str := range strs {
		bits := strings.Count(str, "1")
		zeros := len(str) - bits

		for i := n; i >= bits; i-- {
			for j := m; j >= zeros; j-- {
				if dp[i-bits][j-zeros]+1 > dp[i][j] {
					dp[i][j] = dp[i-bits][j-zeros] + 1
				}
			}
		}
	}
	return dp[n][m]
}
