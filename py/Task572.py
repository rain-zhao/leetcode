# 给定两个非空二叉树 s 和 t，检验 s 中是否包含和 t 具有相同结构和节点值的子树。s 的一个子树包括 s 的一个节点和这个节点的所有子孙。s 也可以看做它自身的一棵子树。

# 示例 1:
# 给定的树 s:

#      3
#     / \
#    4   5
#   / \
#  1   2
# 给定的树 t：

#    4
#   / \
#  1   2
# 返回 true，因为 t 与 s 的一个子树拥有相同的结构和节点值。

# 示例 2:
# 给定的树 s：

#      3
#     / \
#    4   5
#   / \
#  1   2
#     /
#    0
# 给定的树 t：

#    4
#   / \
#  1   2
# 返回 false。


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def check(self, s: TreeNode, t: TreeNode) -> bool:
        if not s:
            return not t
        if not t:
            return False
        if s.val != t.val:
            return False
        return self.check(s.left, t.left) and self.check(s.right, t.right)

    # dfs
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s:
            return not t
        return self.check(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    # dfs打印串
    def isSubtree2(self, s: TreeNode, t: TreeNode) -> bool:
        def dfs(s: TreeNode) -> str:
            if not s:
                return '#'
            return ',' + str(s.val) + dfs(s.left) + dfs(s.right)
        ss = dfs(s)
        st = dfs(t)
        return st in ss
    
    def isSubtree2(self, s: TreeNode, t: TreeNode) -> bool:


s = TreeNode(3)
s.left, s.right = TreeNode(4), TreeNode(5)
s.left.left, s.right.left = TreeNode(1), TreeNode(2)
t = TreeNode(3)
t.left, t.right = TreeNode(1), TreeNode(2)

obj = Solution()
print(obj.isSubtree2(s, t))
