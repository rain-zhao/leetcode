package task231

//recursion
func isPowerOfTwo(n int) bool {
	if n == 1 {
		return true
	}
	if n <= 0 || n&1 == 1 {
		return false
	}
	return isPowerOfTwo(n >> 1)
}

//判断n是否是题目范围最大的2次幂的约数
func isPowerOfTwo2(n int) bool {
	MAX := 1 << 30
	return n > 0 && MAX%n == 0
}

//2的幂次方二进制表示只有一个bit = 1，其余为0
func isPowerOfTwo3(n int) bool {
	return n > 0 && n&(n-1) == 0
}

func isPowerOfTwo4(n int) bool {
	return n > 0 && n&-n == n
}
