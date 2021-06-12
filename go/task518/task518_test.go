package task518

import (
	"testing"
)

func Test_change(t *testing.T) {
	type args struct {
		amount int
		coins  []int
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		// TODO: Add test cases.
		{"test case 1", args{5, []int{1, 2, 5}}, 4},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := change(tt.args.amount, tt.args.coins); got != tt.want {
				t.Errorf("change() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_change2(t *testing.T) {
	type args struct {
		amount int
		coins  []int
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		// TODO: Add test cases.
		{"test case 1", args{5, []int{1, 2, 5}}, 4},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := change2(tt.args.amount, tt.args.coins); got != tt.want {
				t.Errorf("change2() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_change3(t *testing.T) {
	type args struct {
		amount int
		coins  []int
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		// TODO: Add test cases.
		{"test case 1", args{5, []int{1, 2, 5}}, 4},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := change3(tt.args.amount, tt.args.coins); got != tt.want {
				t.Errorf("change3() = %v, want %v", got, tt.want)
			}
		})
	}
}

func Test_change4(t *testing.T) {
	type args struct {
		amount int
		coins  []int
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		// TODO: Add test cases.
		{"test case 1", args{5, []int{1, 2, 5}}, 4},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := change4(tt.args.amount, tt.args.coins); got != tt.want {
				t.Errorf("change4() = %v, want %v", got, tt.want)
			}
		})
	}
}
