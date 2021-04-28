package test

import (
	"fmt"
	"testing"
)

func TestDemo7(t *testing.T) {
	a := []int{1, 2, 3, 4, 5}
	for _, v := range a {
		fmt.Println(v)
	}
}
