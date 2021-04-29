package test

import (
	"fmt"
	"testing"
	"time"
)

func Chann(ch chan int, stopCh chan bool) {
	var i int = 10
	for j := 0; j < 10; j++ {
		ch <- i
		time.Sleep(time.Second)
	}
	stopCh <- true
}

func TestDemo4(t *testing.T) {

	ch := make(chan int)
	var c int
	stopCh := make(chan bool)

	go Chann(ch, stopCh)

	for {
		select {
		case c = <-ch:
			fmt.Println("Receive", c)
			fmt.Println("channel")
		case s := <-ch:
			fmt.Println("Receive", s)
		case <-stopCh:
			goto end
		}
	}
end:
}
