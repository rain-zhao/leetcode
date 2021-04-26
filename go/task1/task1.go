package main

import (
	"fmt"
)

func twoSum(nums []int, target int) []int {
	set := make(map[int]int)
	for p, num := range nums {
		if q, ok := set[num]; ok {
			return []int{p, q}
		}
		set[target-num] = p
	}
	return nil
}

func main() {
	nums := []int{2, 7, 11, 15}
	target := 9
	fmt.Println(twoSum(nums, target))
}
