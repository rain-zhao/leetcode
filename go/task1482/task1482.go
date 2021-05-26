package task1482

import "math"

// binary search
func minDays(bloomDay []int, m int, k int) int {
	
	if len(bloomDay) < m*k {
		return -1
	}

	checkDay := func(days int) bool {
		flowers, combo := 0, 0
		for _, day := range bloomDay {
			if day > days {
				combo = 0
				continue
			}
			combo += 1
			if combo == k {
				flowers += 1
				combo = 0
				if flowers == m {
					return true
				}
			}
		}
		return false
	}

	left, right := math.MaxInt32, math.MinInt32

	// find min,max boundary
	for _, day := range bloomDay {
		if day < left {
			left = day
		}
		if day > right {
			right = day
		}
	}

	//search
	for left <= right {
		mid := (left + right) >> 1
		if checkDay(mid) {
			right = mid - 1
		} else {
			left = mid + 1
		}
	}

	return left

}
