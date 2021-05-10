package test

import (
	"reflect"
	"testing"
)

func TestTypeAndValue(t *testing.T) {
	var f int64 = 10
	t.Log(reflect.TypeOf(f), reflect.ValueOf(f))
	t.Log(reflect.ValueOf(f).Type())
	t.Log(reflect.ValueOf(f).Kind())
	t.Log(reflect.TypeOf(f).Kind())
}

func checkType(v interface{}) string {
	t := reflect.TypeOf(v)
	switch t.Kind() {
	case reflect.Float32, reflect.Float64:
		return "Float"
	case reflect.Int, reflect.Int8, reflect.Int16, reflect.Int32, reflect.Int64:
		return "Integer"
	default:
		return "others"
	}
}

func TestCheckType(t *testing.T) {
	var f int16
	t.Log(checkType(f))
	t.Log(checkType(&f))
	var f1 bool
	t.Log(checkType(f1))
	var f2 float32
	t.Log(checkType(f2))
	var f3 string
	t.Log(checkType(f3))
}

type Employee struct {
	EmployeeId string
	Name       string `format:"nomal"`
	Age        int
}

func (e *Employee) UpdateAge(age int) {
	e.Age = age
}
func (e Employee) UpdateAge1(age int) {
	e.Age = age
}

func TestInvokeByField(t *testing.T) {
	e := &Employee{"1234", "rain.zhao", 20}
	//using reflect get value
	t.Logf("the employee's age is %d\n", reflect.ValueOf(*e).FieldByName("Age").Int())

	if field, ok := reflect.TypeOf(*e).FieldByName("Name"); ok {
		t.Logf("the employee's name's tag is %v\n", field.Tag.Get("format"))
	} else {
		t.Error("field name not found")
	}

	e.UpdateAge(25)
	t.Log("new age is", e.Age)

	//using reflect invoke method
	if method, ok := reflect.TypeOf(e).MethodByName("UpdateAge"); ok {
		method.Func.Call([]reflect.Value{reflect.ValueOf(e), reflect.ValueOf(30)})
	} else {
		t.Error("method not found")
	}
	t.Log("new age is", e.Age)
	//another way
	reflect.ValueOf(e).MethodByName("UpdateAge").Call([]reflect.Value{reflect.ValueOf(35)})
	t.Log("new age is", e.Age)

	reflect.ValueOf(*e).MethodByName("UpdateAge1").Call([]reflect.Value{reflect.ValueOf(40)})
	t.Log("new age is", e.Age)

}

type Customer struct {
	CustomerId string
	Name       string
	Age        int
}

func TestDeepEqual(t *testing.T) {

	//compare map
	a := map[int]string{1: "one", 2: "two", 3: "three"}
	b := map[int]string{1: "one", 2: "two", 3: "three"}

	// t.Log(a == b)
	t.Log(reflect.DeepEqual(a, b))

	//compare slice
	s1 := []int{1, 2, 3}
	s2 := []int{1, 2, 3}
	s3 := []int{1, 2, 4}

	// t.Log(s1 == s2)
	t.Log(reflect.DeepEqual(s1, s2))
	t.Log(reflect.DeepEqual(s1, s3))

	//compare obj
	c1 := Customer{"1", "rain.zhao", 20}
	c2 := Customer{"1", "rain.zhao", 20}

	t.Log(c1 == c2)
	t.Log(reflect.DeepEqual(c1, c2))

}
