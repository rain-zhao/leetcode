package test

import (
	"fmt"
	"sync"
	"testing"
	"time"
)

func produce(ch chan int, wg *sync.WaitGroup) {
	for i := 0; i < 10; i++ {
		ch <- i
	}
	fmt.Println("produce done")
	close(ch)
	wg.Done()
}

func receiver(ch chan int, wg *sync.WaitGroup) {
	for i := 0; i < 10; i++ {
		if data, ok := <-ch; ok {
			fmt.Println(data)
		} else {
			fmt.Println("channel close")
			break
		}
	}
	fmt.Println("receive done")
	wg.Done()
}

func TestChannelProduceAndReceive(t *testing.T) {
	wg := &sync.WaitGroup{}
	ch := make(chan int)
	wg.Add(1)
	go produce(ch, wg)
	wg.Add(1)
	go receiver(ch, wg)
	wg.Add(1)
	go receiver(ch, wg)

	time.Sleep(time.Second * 10)
}
