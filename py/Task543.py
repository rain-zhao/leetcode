
# 给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过根结点。

# 示例 :
# 给定二叉树

#           1
#          / \
#         2   3
#        / \
#       4   5
# 返回 3, 它的长度是路径 [4,2,1,3] 或者 [5,2,1,3]。

# 注意：两结点之间的路径长度是以它们之间边的数目表示。


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # dfs
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.res = 0

        def _dfs(node: TreeNode) -> int:
            if not node:
                return 0
            maxL, maxR = _dfs(node.left), _dfs(node.right)
            self.res = max(self.res, maxL + maxR)
            return max(maxL, maxR) + 1
        _dfs(root)
        return self.res


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

obj = Solution()
print(obj.diameterOfBinaryTree(root))
