package task342

//recursion
func isPowerOfFour(n int) bool {
	if n == 1 {
		return true
	}
	if n <= 0 || n%4 > 0 {
		return false
	}
	return isPowerOfFour(n >> 2)
}

func isPowerOfFour2(n int) bool {
	if n <= 0 || n&-n != n {
		return false
	}
	for n > 0 {
		if n == 1 {
			return true
		}
		n >>= 2
	}
	return false
}

func isPowerOfFour3(n int) bool {
	return n > 0 && n&-n == n && n&0xaaaaaaaa == 0
}
