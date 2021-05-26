package task137

func singleNumber(nums []int) int {
	set := map[int]bool{}
	sum1, sum2 := 0, 0
	for _, num := range nums {
		set[num] = true
		sum1 += num
	}
	for num := range set {
		sum2 += num
	}
	return (sum2*3 - sum1) >> 1
}

func singleNumber2(nums []int) int {
	dict := map[int]int{}
	for _, num := range nums {
		dict[num] += 1
	}
	for k, v := range dict {
		if v == 1 {
			return k
		}
	}
	return -1
}

// bit op
func singleNumber3(nums []int) int {
	ones, twos := 0, 0
	for _, num := range nums {
		ones = ones ^ num & ^twos
		twos = twos ^ num & ^ones
	}
	return ones
}
