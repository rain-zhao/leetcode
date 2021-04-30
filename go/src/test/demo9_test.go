package test

import (
	"testing"
)

func Test_demo9(t *testing.T) {
	var s string
	if s == "" {
		t.Log("s is equal to \"\"")
	}

	a := [...]int{1, 2, 3}
	b := [...]int{1, 2, 3}

	t.Log(a == b)
	t.Log(&a == &b)
}

func TestSilce(t *testing.T) {
	s := make([]int, 0, 3)
	t.Log(len(s), cap(s))

	if s == nil {
		t.Log("切片是空的")
	}
	s = append(s, 1)
	t.Log(len(s), cap(s))

	s = append(s, 2)
	t.Log(len(s), cap(s))
	s = append(s, 3)
	t.Log(len(s), cap(s))
	s = append(s, 4)
	t.Log(len(s), cap(s))
	s = append(s, 5)
	t.Log(len(s), cap(s))

}

func TestSilceShare(t *testing.T) {

	s := []int{0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}
	t.Log(len(s), cap(s))

	s1 := s[3:6]
	t.Log(len(s1), cap(s1))

	s2 := s[7:9]
	t.Log(len(s2), cap(s2))

	s2 = append(s2, 12)
	t.Log(len(s), cap(s), s)
	t.Log(len(s2), cap(s2), s2)

}
