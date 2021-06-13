package task1449

import "testing"

func Test_largestNumber(t *testing.T) {
	type args struct {
		cost   []int
		target int
	}
	tests := []struct {
		name string
		args args
		want string
	}{
		// TODO: Add test cases.
		{"test case 1", args{[]int{4, 3, 2, 5, 6, 7, 2, 5, 5}, 9}, "7772"},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := largestNumber(tt.args.cost, tt.args.target); got != tt.want {
				t.Errorf("largestNumber() = %v, want %v", got, tt.want)
			}
		})
	}
}
