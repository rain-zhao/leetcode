package test

import (
	"fmt"
	"runtime"
	"testing"
	"time"
)

func runTask(id int) string {
	time.Sleep(time.Millisecond * 100)
	return fmt.Sprintf("task result from %d \n", id)
}

func firstRespond() string {
	ch := make(chan string, 10)
	for i := 0; i < 10; i++ {
		go func(id int) {
			ch <- runTask(id)
		}(i)
	}
	return <-ch
}

func allRespond() string {
	ch := make(chan string, 10)
	for i := 0; i < 10; i++ {
		go func(id int) {
			ch <- runTask(id)
		}(i)
	}

	finalResp := ""
	for i := 0; i < 10; i++ {
		finalResp += <-ch
	}

	return finalResp
}

func TestAllRespond(t *testing.T) {
	fmt.Println("before:", runtime.NumGoroutine())
	fmt.Println(allRespond())
	fmt.Println("after:", runtime.NumGoroutine())
}

func TestFirstRespond(t *testing.T) {
	fmt.Println("before:", runtime.NumGoroutine())
	fmt.Println(firstRespond())
	fmt.Println("after:", runtime.NumGoroutine())
}
