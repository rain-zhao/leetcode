package test

import (
	"testing"
)

func TestMapExt(t *testing.T) {
	stratery := map[int]func(op int) int{}
	stratery[0] = func(op int) int { return op }
	stratery[1] = func(op int) int { return op * op }
	stratery[2] = func(op int) int { return op * op * op }

	for i := 0; i < 3; i++ {
		t.Log(stratery[i](2))
	}
}

