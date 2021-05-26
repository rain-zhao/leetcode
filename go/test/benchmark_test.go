package test

import (
	"bytes"
	"testing"

	"github.com/stretchr/testify/assert"
)

func TestConcatStrByAdd(t *testing.T) {
	assert := assert.New(t)

	eles := [...]string{"1", "2", "3", "4", "5"}
	res := ""
	for _, ele := range eles {
		res += ele
	}
	assert.Equal("12345", res, "error")
}

func TestConcatStrByBuffer(t *testing.T) {
	assert := assert.New(t)

	eles := [...]string{"1", "2", "3", "4", "5"}
	buff := &bytes.Buffer{}
	for _, ele := range eles {
		buff.WriteString(ele)
	}
	assert.Equal("12345", buff.String(), "error")
}

func BenchmarkConcatStrByAdd(b *testing.B) {
	eles := [...]string{"1", "2", "3", "4", "5"}
	b.StartTimer()
	for i := 0; i < b.N; i++ {
		res := ""
		for _, ele := range eles {
			res += ele
		}
	}
	b.StopTimer()
}

func BenchmarkConcatStrByBuffer(b *testing.B) {
	eles := [...]string{"1", "2", "3", "4", "5"}
	b.StartTimer()
	for i := 0; i < b.N; i++ {
		buff := &bytes.Buffer{}
		for _, ele := range eles {
			buff.WriteString(ele)
		}
	}
	b.StopTimer()
}
