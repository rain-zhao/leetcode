package task1310

import (
	"reflect"
	"testing"
)

func Test_xorQueries(t *testing.T) {
	type args struct {
		arr     []int
		queries [][]int
	}
	tests := []struct {
		name string
		args args
		want []int
	}{
		// TODO: Add test cases.
		{"test case 1", args{[]int{1, 3, 4, 8}, [][]int{{0, 1}, {1, 2}, {0, 3}, {3, 3}}}, []int{2, 7, 14, 8}},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := xorQueries(tt.args.arr, tt.args.queries); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("xorQueries() = %v, want %v", got, tt.want)
			}
		})
	}
}
