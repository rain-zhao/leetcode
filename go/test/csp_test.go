package test

import (
	"fmt"
	"testing"
	"time"
)

func service() string {
	fmt.Println("service do something...")
	time.Sleep(time.Microsecond * 100)
	fmt.Println("service done")
	return "service done"
}

func otherService() {
	fmt.Println("other service do something...")
	time.Sleep(time.Microsecond * 100)
	fmt.Println("other service done")
}

func TestSyncService(t *testing.T) {
	ret := service()
	otherService()
	fmt.Println(ret)
}

func asyncService() chan string {
	fmt.Println("async service start")
	ret := make(chan string, 1)
	go func() {
		out := service()
		fmt.Println("async service return result")
		ret <- out
		time.Sleep(time.Microsecond * 100)
		fmt.Println("async service exited")
	}()
	return ret
}

func TestAsyncService(t *testing.T) {
	ret := asyncService()
	otherService()
	time.Sleep(time.Microsecond * 1000)
	fmt.Println(<-ret)
	time.Sleep(time.Microsecond * 200)
}
