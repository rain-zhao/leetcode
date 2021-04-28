package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func rangeSumBST(root *TreeNode, low int, high int) int {
	if root == nil {
		return 0
	}
	res := 0
	if low <= root.Val && root.Val <= high {
		res += root.Val + rangeSumBST(root.Left, low, high) + rangeSumBST(root.Right, low, high)
	} else if root.Val < low {
		res += rangeSumBST(root.Right, low, high)
	} else if root.Val > high {
		res += rangeSumBST(root.Left, low, high)
	}
	return res
}

func main() {
	low := 6
	high := 10
	root := TreeNode{10, &TreeNode{Val: 5}, &TreeNode{Val: 15}}
	root.Left.Left = &TreeNode{Val: 3, Left: &TreeNode{Val: 1}}
	root.Left.Right = &TreeNode{Val: 7, Left: &TreeNode{Val: 6}}
	root.Right.Left = &TreeNode{Val: 13}
	root.Right.Right = &TreeNode{Val: 18}

	println(rangeSumBST(&root, low, high))

}
