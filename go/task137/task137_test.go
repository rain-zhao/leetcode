package task137

import (
	"testing"
)

func Test_singleNumber(t *testing.T) {
	type args struct {
		nums []int
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		// TODO: Add test cases.
		{"test case 1", args{[]int{0, 1, 0, 1, 0, 1, 99}}, 99},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := singleNumber(tt.args.nums); got != tt.want {
				t.Errorf("singleNumber() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_singleNumber2(t *testing.T) {
	type args struct {
		nums []int
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		// TODO: Add test cases.
		{"test case 1", args{[]int{0, 1, 0, 1, 0, 1, 99}}, 99},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := singleNumber2(tt.args.nums); got != tt.want {
				t.Errorf("singleNumber2() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_singleNumber3(t *testing.T) {
	type args struct {
		nums []int
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		// TODO: Add test cases.
		{"test case 1", args{[]int{0, 1, 0, 1, 0, 1, 99}}, 99},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := singleNumber3(tt.args.nums); got != tt.want {
				t.Errorf("singleNumber3() = %v, want %v", got, tt.want)
			}
		})
	}
}
