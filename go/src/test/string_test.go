package test

import (
	"strconv"
	"testing"
)

func TestStrconv(t *testing.T) {

	s := strconv.Itoa(10)
	s1 := strconv.FormatInt(10, 2)
	s2 := strconv.FormatInt(10, 10)
	t.Log(s, s1, s2)

	a, _ := strconv.Atoi("10")
	a1, _ := strconv.ParseInt("10", 10, 0)
	a2, _ := strconv.ParseInt("10", 2, 0)
	a3, _ := strconv.ParseInt("ae", 16, 0)
	t.Log(a, a1, a2, a3)

}
