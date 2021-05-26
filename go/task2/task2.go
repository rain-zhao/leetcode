package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {

	if l1.Val == 0 && l1.Next == nil {
		return l2
	}
	if l2.Val == 0 && l2.Next == nil {
		return l1
	}

	carry := 0

	dummy := new(ListNode)
	p1, p2, pre := l1, l2, dummy

	for p1 != nil || p2 != nil {
		v1, v2 := 0, 0

		if p1 != nil {
			v1 = p1.Val
			p1 = p1.Next
		}

		if p2 != nil {
			v2 = p2.Val
			p2 = p2.Next
		}

		sum := v1 + v2 + carry
		pre.Next = &ListNode{Val: sum % 10}
		carry = sum / 10
		pre = pre.Next
	}

	if carry == 1 {
		pre.Next = &ListNode{Val: 1}
	}

	return dummy.Next
}

func main() {
	l1 := ListNode{Val: 2, Next: &ListNode{Val: 4, Next: &ListNode{Val: 9}}}
	l2 := ListNode{Val: 5, Next: &ListNode{Val: 6, Next: &ListNode{Val: 4, Next: &ListNode{Val: 9}}}}

	l3 := addTwoNumbers(&l1, &l2)
	fmt.Println(l3)
}
