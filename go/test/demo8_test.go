package test

import (
	"fmt"
	"testing"
	"time"
)

var sep = time.Second * 1

func sum(s []int, c chan int) {
	sum := 0
	for _, v := range s {
		sum += v
	}
	time.Sleep(sep)
	sep *= 2
	c <- sum // 把 sum 发送到通道 c
}

func TestDemo8(t *testing.T) {
	s := []int{7, 2, 8, -9, 4, 0}

	c := make(chan int)
	go sum(s[:len(s)/2], c)
	go sum(s[len(s)/2:], c)
	x, y := <-c, <-c // 从通道 c 中接收

	fmt.Println(x, y, x+y)
}
