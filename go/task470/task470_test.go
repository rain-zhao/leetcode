package task470

import "testing"

func Test_rand10(t *testing.T) {
	r1, r2 := rand10(), rand10()
	t.Log(r1, r2, r1 == r2)
}
