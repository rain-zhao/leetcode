package test

import (
	"context"
	"fmt"
	"sync"
	"testing"
	"time"
)

func isCanceled(ctx context.Context) bool {
	select {
	case <-ctx.Done():
		return true
	default:
		return false
	}
}
func TestContextCancel(t *testing.T) {
	ctx, cancel := context.WithCancel(context.Background())
	wg := &sync.WaitGroup{}
	wg.Add(5)
	for i := 0; i < 5; i++ {
		go func(i int, ctx context.Context, wg *sync.WaitGroup) {
			for {
				if isCanceled(ctx) {
					fmt.Println(i, " task canceled")
					break
				}
				time.Sleep(time.Second * 1)
			}
			wg.Done()

		}(i, ctx, wg)
	}

	cancel()
	wg.Wait()
	fmt.Println("all task has been cancel")

}
