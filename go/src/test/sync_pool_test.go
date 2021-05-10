package test

import (
	"sync"
	"testing"
	"time"
)

func TestSyncPool(t *testing.T) {
	pool := &sync.Pool{
		New: func() interface{} {
			println("create new obj")
			return 100
		},
	}

	v := pool.Get().(int)
	println(v)

	pool.Put(10)
	pool.Put(20)
	pool.Put(30)

	for i := 0; i < 10; i++ {
		go func() {
			println(pool.Get().(int))
		}()
	}

	time.Sleep(time.Second * 1)

}
