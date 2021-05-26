package test

import "testing"

func TestDeferFunc(t *testing.T) {
	defer func() {
		t.Log("clean resource!")
	}()

	t.Log("started")
	panic("fatal error")

}
