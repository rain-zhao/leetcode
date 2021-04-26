package main

import "fmt"

func main() {
    // 声明一个变量并初始化
    var a = "RUNOOB"
    fmt.Println(a)

    // 没有初始化就为零值
    var b int
    fmt.Println(b)

	//string 初始值为空字符串（跟java不同）
    var c string
    fmt.Println(c)

	// bool 零值为 false
	var d bool
	fmt.Println(d)
}
