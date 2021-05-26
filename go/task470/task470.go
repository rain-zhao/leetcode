package task470

import "math/rand"

func rand7() int {
	return rand.Intn(7) + 1
}

func rand10() int {
	idx := 49
	for idx > 40 {
		row, col := rand7(), rand7()
		idx = col + 7*(row-1)
	}
	return idx%10 + 1
}
