package task518

import (
	"fmt"
)

// dfs
func change(amount int, coins []int) int {
	if amount == 0 {
		return 1
	}
	if amount < 0 {
		return 0
	}
	res := 0
	for i, coin := range coins {
		res += change(amount-coin, coins[i:])
	}
	return res
}

// dfs + memory
func change2(amount int, coins []int) int {
	dict := make(map[string]int)

	var dfs func(amount, i int) int

	dfs = func(amount, i int) int {
		key := fmt.Sprintf("%d,%d", amount, i)

		if val, ok := dict[key]; ok {
			return val
		}

		if amount == 0 {
			dict[key] = 1
			return 1
		}
		if amount < 0 {
			dict[key] = 0
			return 0
		}
		res := 0

		for ii, coin := range coins[i:] {
			res += dfs(amount-coin, i+ii)
		}
		dict[key] = res
		return res
	}

	return dfs(amount, 0)

}

// dp[i][j] := amount = i and remain j kinds of coins
func change3(amount int, coins []int) int {
	// define
	dp := make([][]int, amount+1)
	n := len(coins)
	// init
	for i := 0; i <= amount; i++ {
		dp[i] = make([]int, n+1)
	}
	// dp[0][k] = 1
	for i := 0; i <= n; i++ {
		dp[0][i] = 1
	}
	// loop
	for i := 1; i <= amount; i++ {
		for j := 1; j <= n; j++ {
			for k := 0; k < j; k++ {
				if i-coins[k] >= 0 {
					dp[i][j] += dp[i-coins[k]][k+1]
				}
			}
		}
	}
	return dp[amount][n]
}

// dp one dimension
func change4(amount int, coins []int) int {
	dp := make([]int, amount+1)
	dp[0] = 1
	for _, coin := range coins {
		for i := coin; i <= amount; i++ {
			dp[i] += dp[i-coin]
		}
	}
	return dp[amount]
}
