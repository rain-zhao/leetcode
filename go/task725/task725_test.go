package task725

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func Test_splitListToParts(t *testing.T) {
	// head := &ListNode{Val: 1}
	// head.NextItem(2).NextItem(3).NextItem(4).NextItem(5).NextItem(6).NextItem(7).NextItem(8).NextItem(9).NextItem(10)

	// got := splitListToParts(head, 3)

	// assert.Equal(t, 3, len(got))
	// assert.Equal(t, 4, got[0].Len())
	// assert.Equal(t, 3, got[1].Len())
	// assert.Equal(t, 3, got[2].Len())

	head := &ListNode{Val: 1}
	head.NextItem(2)

	got := splitListToParts(head, 3)

	assert.Equal(t, 3, len(got))
	assert.Equal(t, 1, got[0].Len())
	assert.Equal(t, 1, got[1].Len())
	assert.Equal(t, 0, got[2].Len())
}
