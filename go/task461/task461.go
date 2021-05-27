package task461

func hammingDistance(x int, y int) int {
	xor := x ^ y
	mask := 1
	res := 0
	for xor > 0 {
		if i := xor & mask; i > 0 {
			xor = xor & ^mask
			res++
		}
		mask <<= 1
	}
	return res
}

func hammingDistance2(x int, y int) int {
	res := 0
	for xor := x ^ y; xor > 0; xor &= xor - 1 {
		res += 1
	}
	return res
}
