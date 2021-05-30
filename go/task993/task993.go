package task993

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func isCousins(root *TreeNode, x int, y int) bool {
	var p1, p2, l1, l2 int
	var dfs func(root *TreeNode, lev int)
	dfs = func(root *TreeNode, lev int) {
		if root == nil {
			return
		}
		if root.Left != nil {
			if left := root.Left; left.Val == x {
				p1, l1 = root.Val, lev+1
			} else if left.Val == y {
				p2, l2 = root.Val, lev+1
			}
		}

		if root.Right != nil {
			if right := root.Right; right.Val == x {
				p1, l1 = root.Val, lev+1
			} else if right.Val == y {
				p2, l2 = root.Val, lev+1
			}
		}

		dfs(root.Left, lev+1)
		dfs(root.Right, lev+1)
	}
	dfs(root, 0)
	return p1 != p2 && l1 == l2

}

func isCousins2(root *TreeNode, x int, y int) bool {
	var p1, p2 *TreeNode
	var l1, l2 int
	var dfs func(root *TreeNode, p *TreeNode, lev int)
	dfs = func(root, p *TreeNode, lev int) {
		if root == nil {
			return
		}
		
		if root.Val == x {
			p1, l1 = p, lev
		} else if root.Val == y {
			p2, l2 = p, lev
		}

		if p1 != nil && p2 != nil {
			return
		}
		dfs(root.Left, root, lev+1)

		if p1 != nil && p2 != nil {
			return
		}
		dfs(root.Right, root, lev+1)
	}
	dfs(root, nil, 0)
	return p1 != p2 && l1 == l2

}
