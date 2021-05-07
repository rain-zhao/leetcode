package test

import (
	"fmt"
	"sync"
	"testing"
	"unsafe"
)

type Singleton struct {
	data string
}

var instance *Singleton
var once sync.Once

func GetInstance() *Singleton {
	once.Do(func() {
		fmt.Println("new instance")
		instance = new(Singleton)
		instance.data = "created"
	})
	return instance
}

func TestCreateSingleton(t *testing.T) {
	var wg sync.WaitGroup
	wg.Add(10)
	for i := 0; i < 10; i++ {
		go func(i int, wg *sync.WaitGroup) {
			ins := GetInstance()
			fmt.Printf("%d instance address %v \n", i, unsafe.Pointer(ins))
			wg.Done()
		}(i, &wg)
	}
	wg.Wait()
}
