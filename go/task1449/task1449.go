package task1449

import "strconv"

// dp
func largestNumber(cost []int, target int) string {
	// define
	dp := make([]string, target+1)
	//init
	dp[0] = ""
	for i := 1; i <= target; i++ {
		dp[i] = "0"
	}
	// loop
	for v, c := range cost {
		v += 1
		for i := c; i <= target; i++ {
			if dp[i-c] != "0" {
				dp[i] = max(dp[i], strconv.Itoa(v)+dp[i-c])
			}
		}

	}
	return dp[target]
}

func max(a, b string) string {
	if len(a) == len(b) {
		if a > b {
			return a
		}
		return b
	}
	if len(a) > len(b) {
		return a
	}
	return b
}
