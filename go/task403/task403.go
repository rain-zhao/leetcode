package task403

// dp using map
func canCross(stones []int) bool {
	n := len(stones)
	dp := map[int]map[int]bool{}
	dp[0] = map[int]bool{0: true}
	for _, stone := range stones[:n-1] {
		if dict, ok := dp[stone]; ok {
			for k := range dict {
				for t := -1; t < 2; t++ {
					if k+t > 0 {
						if dp[stone+k+t] == nil {
							dp[stone+k+t] = map[int]bool{}
						}
						dp[stone+k+t][k+t] = true
					}
				}
			}
		}
	}
	//last stone
	return dp[stones[n-1]] != nil
}

// dp using array
func canCross2(stones []int) bool {
	n := len(stones)

	// define
	dp := make([][]bool, n)

	for i := range dp {
		dp[i] = make([]bool, n)
	}

	//init
	dp[0][0] = true

	// iter
	for i := 1; i < n; i++ {
		for j := i - 1; j >= 0; j-- {
			k := stones[i] - stones[j]
			if k > j+1 {
				break
			}
			dp[i][k] = dp[j][k-1] || dp[j][k] || dp[j][k+1]
		}
	}
	//check dp[n-1]
	for _, ok := range dp[n-1] {
		if ok {
			return true
		}
	}
	return false
}
