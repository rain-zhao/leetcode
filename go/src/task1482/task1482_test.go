package task1482

import "testing"

func Test_minDays(t *testing.T) {
	type args struct {
		bloomDay []int
		m        int
		k        int
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		// TODO: Add test cases.
		{"test case 1", args{[]int{1, 10, 3, 10, 2}, 3, 1}, 3},
		{"test case 2", args{[]int{1, 10, 3, 10, 2}, 3, 2}, -1},
		{"test case 3", args{[]int{7, 7, 7, 7, 12, 7, 7}, 2, 3}, 12},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := minDays(tt.args.bloomDay, tt.args.m, tt.args.k); got != tt.want {
				t.Errorf("minDays() = %v, want %v", got, tt.want)
			}
		})
	}
}
