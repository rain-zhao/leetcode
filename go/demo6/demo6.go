package main

import "fmt"

type User struct {
	name string
	sex  string
}

func (user User) changeName(newName string) {
	user.name = newName
}

func (user *User) changeName2(newName string) {
	user.name = newName
}

func main() {
	////////////方法参数为对象///////////////
	user := User{"rian.zhao", "male"}

	fmt.Println(user.name)

	user.changeName("Rain.Zhao")

	fmt.Println(user.name)

	u := &user

	fmt.Println(u.name)

	u.changeName("Rain.Zhao")

	fmt.Println(u.name)

	//////////////////方法参数为指针///////////////////////////////
	user2 := User{"rian.zhao", "male"}

	fmt.Println(user2.name)

	user2.changeName2("Rain.Zhao")

	fmt.Println(user2.name)

	u2 := new(User)

	fmt.Println(u2.name)

	u2.changeName2("Rain.Zhao")

	fmt.Println(u2.name)

}
