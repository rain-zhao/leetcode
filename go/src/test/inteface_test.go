package test

import (
	"fmt"
	"testing"
)

type SchoolMate interface {
	sayHello()
}

type Student struct {
	name string
}

func (st *Student) sayHello() {
	fmt.Printf("hello World! %v\n", st.name)
}

type Teacher struct {
	title string
}

func (t *Teacher) sayHello() {
	fmt.Printf("hello World! %v\n", t.title)
}

func TestInteface(t *testing.T) {
	var mate SchoolMate

	mate = &Student{"rain.zhao"}
	mate.sayHello()

	mate = &Teacher{"master"}
	mate.sayHello()
}
