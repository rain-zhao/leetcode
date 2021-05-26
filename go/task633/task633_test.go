package task633

import (
	"testing"
)

func Test_judgeSquareSum(t *testing.T) {
	type args struct {
		c int
	}
	tests := []struct {
		name string
		args args
		want bool
	}{
		// TODO: Add test cases.
		// {"test case 1",args{5},true},
		// {"test case 2",args{3},false},
		// {"test case 3",args{2},true},
		{"test case 4", args{1}, true},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := judgeSquareSum(tt.args.c); got != tt.want {
				t.Errorf("judgeSquareSum() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_judgeSquareSum2(t *testing.T) {
	type args struct {
		c int
	}
	tests := []struct {
		name string
		args args
		want bool
	}{
		// TODO: Add test cases.
		{"test case 1", args{5}, true},
		{"test case 2", args{3}, false},
		{"test case 3", args{2}, true},
		{"test case 4", args{1}, true},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := judgeSquareSum2(tt.args.c); got != tt.want {
				t.Errorf("judgeSquareSum2() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_judgeSquareSum3(t *testing.T) {
	type args struct {
		c int
	}
	tests := []struct {
		name string
		args args
		want bool
	}{
		// TODO: Add test cases.
		{"test case 1", args{5}, true},
		{"test case 2", args{3}, false},
		{"test case 3", args{2}, true},
		{"test case 4", args{1}, true},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := judgeSquareSum3(tt.args.c); got != tt.want {
				t.Errorf("judgeSquareSum3() = %v, want %v", got, tt.want)
			}
		})
	}
}
