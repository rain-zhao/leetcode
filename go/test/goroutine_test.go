package test

import (
	"sync"
	"testing"
	"time"
)

func TestGoroutine(t *testing.T) {

	for i := 0; i < 100; i++ {
		// go func(i int) {
		// 	println(i)
		// }(i)
		go func(i int) {
			println(i)
		}(i)
	}
	time.Sleep(time.Second * 10)
}

func TestGoroutineThreadSafe(t *testing.T) {
	counter := 0
	mutex := sync.Mutex{}
	for i := 0; i < 5000; i++ {
		go func() {
			defer func() {
				mutex.Unlock()
			}()
			mutex.Lock()
			counter++
		}()
	}

	time.Sleep(time.Second * 1)
	println(counter)
}

func TestGoroutineWaitGroup(t *testing.T) {
	counter := 0
	mutex := sync.Mutex{}
	wg := sync.WaitGroup{}
	wg.Add(5000)
	for i := 0; i < 5000; i++ {
		go func() {
			defer func() {
				mutex.Unlock()
			}()
			mutex.Lock()
			counter++
			wg.Done()
		}()
	}

	wg.Wait()
	println(counter)
}
