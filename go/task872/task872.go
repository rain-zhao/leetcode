package task872

import "reflect"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func leafSimilar(root1 *TreeNode, root2 *TreeNode) bool {
	var dfs func(root *TreeNode, leaves []int) []int
	dfs = func(root *TreeNode, leaves []int) []int {
		if root == nil {
			return leaves
		}

		if root.Left == nil && root.Right == nil {
			return append(leaves, root.Val)
		}

		leaves = dfs(root.Left, leaves)
		leaves = dfs(root.Right, leaves)

		return leaves
	}

	l1, l2 := []int{}, []int{}

	l1 = dfs(root1, l1)
	l2 = dfs(root2, l2)

	return reflect.DeepEqual(l1, l2)

}
