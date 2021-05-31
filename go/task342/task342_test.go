package task342

import (
	"testing"
)

func Test_isPowerOfFour(t *testing.T) {
	type args struct {
		n int
	}
	tests := []struct {
		name string
		args args
		want bool
	}{
		// TODO: Add test cases.
		{"test case 1", args{16}, true},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := isPowerOfFour(tt.args.n); got != tt.want {
				t.Errorf("isPowerOfFour() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_isPowerOfFour2(t *testing.T) {
	type args struct {
		n int
	}
	tests := []struct {
		name string
		args args
		want bool
	}{
		// TODO: Add test cases.
		{"test case 1", args{16}, true},
		{"test case 2", args{5}, false},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := isPowerOfFour2(tt.args.n); got != tt.want {
				t.Errorf("isPowerOfFour2() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_isPowerOfFour3(t *testing.T) {
	type args struct {
		n int
	}
	tests := []struct {
		name string
		args args
		want bool
	}{
		// TODO: Add test cases.
		{"test case 1", args{16}, true},
		{"test case 2", args{5}, false},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := isPowerOfFour3(tt.args.n); got != tt.want {
				t.Errorf("isPowerOfFour3() = %v, want %v", got, tt.want)
			}
		})
	}
}
