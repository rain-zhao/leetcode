# 给定一个二叉搜索树（Binary Search Tree），把它转换成为累加树（Greater Tree)，使得每个节点的值是原来的节点值加上所有大于它的节点值之和。

#  

# 例如：

# 输入: 原始二叉搜索树:
#               5
#             /   \
#            2     13

# 输出: 转换为累加树:
#              18
#             /   \
#           20     13

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # dfs
    def convertBST(self, root: TreeNode) -> TreeNode:
        total = 0

        def dfs(root: TreeNode):
            if not root:
                return
            dfs(root.right)
            nonlocal total
            total += root.val
            root.val = total
            dfs(root.left)
        dfs(root)
        return root


root = TreeNode(5)
root.left = TreeNode(2)
root.right = TreeNode(13)

obj = Solution()
print(obj.convertBST(root))
