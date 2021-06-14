package task374

// binary search
func guessNumber(n int) int {
	left, right := 1, n
	for left <= right {
		mid := left + (right-left)>>1
		if guess(mid) == 0 {
			return mid
		} else if guess(mid) < 0 {
			right = mid - 1
		} else {
			left = mid + 1
		}
	}
	return -1
}
