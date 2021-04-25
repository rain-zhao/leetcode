# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        pre = dummy = TreeNode(-1)

        def dfs(root: TreeNode):
            if not root:
                return
            dfs(root.left)
            nonlocal pre
            pre.right = root
            root.left = None
            pre = pre.right
            dfs(root.right)
        dfs(root)
        return dummy.right
