package test

import (
	"fmt"
	"testing"
)

type A struct {
	aint int
	b    *B
}

type B struct {
	bint int
}

func TestEmptyValue(t *testing.T) {
	a := A{}
	fmt.Println(a.aint)
	//invalid memory address or nil pointer dereference
	fmt.Println(a.b.bint)
}
