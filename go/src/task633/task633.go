package task633

import "math"

func judgeSquareSum(c int) bool {
	appear := make(map[int]bool)
	for i := 0; i*i <= c; i++ {
		appear[c-i*i] = true
		if _, ok := appear[i*i]; ok {
			return true
		}
	}
	return false
}

func judgeSquareSum2(c int) bool {
	for i := 0; i*i <= c; i++ {
		b := math.Sqrt(float64(c - i*i))
		if b == math.Floor(b) {
			return true
		}
	}
	return false
}

func judgeSquareSum3(c int) bool {
	left, right := 0, int(math.Sqrt(float64(c)))
	for left <= right {
		sum := left*left + right*right
		if sum == c {
			return true
		} else if sum < c {
			left++
		} else {
			right--
		}
	}
	return false
}
