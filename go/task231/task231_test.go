package task231

import (
	"testing"
)

func Test_isPowerOfTwo(t *testing.T) {
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
			if got := isPowerOfTwo(tt.args.n); got != tt.want {
				t.Errorf("isPowerOfTwo() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_isPowerOfTwo2(t *testing.T) {
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
			if got := isPowerOfTwo2(tt.args.n); got != tt.want {
				t.Errorf("isPowerOfTwo2() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_isPowerOfTwo3(t *testing.T) {
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
			if got := isPowerOfTwo3(tt.args.n); got != tt.want {
				t.Errorf("isPowerOfTwo2() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_isPowerOfTwo4(t *testing.T) {
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
			if got := isPowerOfTwo4(tt.args.n); got != tt.want {
				t.Errorf("isPowerOfTwo4() = %v, want %v", got, tt.want)
			}
		})
	}
}
