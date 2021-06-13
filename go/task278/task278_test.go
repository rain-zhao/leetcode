package task278

import (
	"reflect"
	"testing"
)

func Test_firstBadVersionClosure(t *testing.T) {
	type args struct {
		n int
		v int
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		// TODO: Add test cases.
		{"test case 1", args{5, 4}, 4},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := firstBadVersionClosure(tt.args.n, tt.args.v); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("firstBadVersionClosure() = %v, want %v", got, tt.want)
			}
		})
	}
}
