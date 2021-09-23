package task725

//   Definition for singly-linked list.
type ListNode struct {
	Val  int
	Next *ListNode
}

func (n *ListNode) NextItem(val int) *ListNode {
	n.Next = &ListNode{Val: val}
	return n.Next
}

func (n *ListNode) Len() int {
	len := 0
	cur := n
	for cur != nil {
		len++
		cur = cur.Next
	}

	return len
}

// two traversal
func splitListToParts(head *ListNode, k int) []*ListNode {
	res := make([]*ListNode, k)
	if head == nil {
		return res
	}

	// 1.traversal to find len of list
	cur := head
	len := 0
	for cur != nil {
		len++
		cur = cur.Next
	}

	// 2. get len of k slice
	m2 := len / k
	m1 := m2 + 1
	n1 := len % k
	n2 := k - n1

	// 3. traversal to split the link list
	cur = head
	for i := 0; i < n1; i++ {
		res[i] = head
		for j := 1; j < m1; j++ {
			cur = cur.Next
		}
		head = cur.Next
		cur.Next = nil
		cur = head
	}

	if m2 == 0 {
		return res
	}

	for i := 0; i < n2; i++ {
		res[n1+i] = head
		for j := 1; j < m2; j++ {
			cur = cur.Next
		}
		head = cur.Next
		cur.Next = nil
		cur = head
	}

	return res

}


func splitListToParts2(head *ListNode, k int) []*ListNode {
    n := 0
    for node := head; node != nil; node = node.Next {
        n++
    }
    quotient, remainder := n/k, n%k

    parts := make([]*ListNode, k)
    for i, curr := 0, head; i < k && curr != nil; i++ {
        parts[i] = curr
        partSize := quotient
        if i < remainder {
            partSize++
        }
        for j := 1; j < partSize; j++ {
            curr = curr.Next
        }
        curr, curr.Next = curr.Next, nil
    }
    return parts
}
