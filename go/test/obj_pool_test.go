package test

import (
	"errors"
	"fmt"
	"testing"
	"time"
)

type ReusableObj struct{}

type ObjPool struct {
	bufCh chan *ReusableObj
}

func newObjPool(size int) *ObjPool {
	pool := new(ObjPool)
	pool.bufCh = make(chan *ReusableObj, size)

	for i := 0; i < size; i++ {
		pool.bufCh <- new(ReusableObj)
	}
	return pool
}

func (p *ObjPool) getObj() (*ReusableObj, error) {
	select {
	case obj := <-p.bufCh:
		return obj, nil
	case <-time.After(time.Second * 1):
		return nil, errors.New("time out when get obj from objpool")
	}
}

func (p *ObjPool) ReleaseObj(obj *ReusableObj) error {
	select {
	case p.bufCh <- obj:
		return nil
	case <-time.After(time.Second * 1):
		return errors.New("time out when release to objpool")
	}
}

func TestObjPool(t *testing.T) {
	pool := newObjPool(5)
	//over size
	// if err := pool.ReleaseObj(new(ReusableObj)); err != nil {
	// 	t.Error(err)
	// }

	for i := 0; i < 5; i++ {
		if obj, err := pool.getObj(); err != nil {
			t.Error(err)
		} else {
			fmt.Println(obj)
		}
	}

	//over size
	// for i := 0; i < 6; i++ {
	// 	if obj, err := pool.getObj(); err != nil {
	// 		t.Error(err)
	// 	} else {
	// 		fmt.Println(obj)
	// 	}
	// }

}
