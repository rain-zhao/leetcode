package test

import (
	"errors"
	"reflect"
	"testing"
)

func fillBySettings(st interface{}, settings map[string]interface{}) error {

	if settings == nil {
		return errors.New("settings must be not null")
	}

	if kind := reflect.TypeOf(st).Kind(); kind != reflect.Ptr {
		return errors.New("type must be ptr")
	}

	if kind := reflect.ValueOf(st).Elem().Kind(); kind != reflect.Struct {
		return errors.New("type must be ptr type point to struct type")
	}

	for k, v := range settings {
		var field reflect.StructField
		var ok bool
		if field, ok = reflect.TypeOf(st).Elem().FieldByName(k); !ok {
			continue
		}
		if field.Type == reflect.TypeOf(v) {
			reflect.ValueOf(st).Elem().FieldByName(k).Set(reflect.ValueOf(v))
		}
	}
	return nil
}

func TestFillBySettings(t *testing.T) {
	settings := map[string]interface{}{"Name": "rain.zhao", "Age": 30, "CustomerId": "123", "EmployeeId": "12"}

	e := Employee{}

	c := Customer{}

	if err := fillBySettings(&e, settings); err != nil {
		t.Error(err)
	} else {
		t.Log(e)
	}

	if err := fillBySettings(&c, settings); err != nil {
		t.Error(err)
	} else {
		t.Log(c)
	}
}
