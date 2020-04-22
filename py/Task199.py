from TreeNode import TreeNode
from typing import List
from collections import deque


class Solution:
    # 1 bfs
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = []
        queue = deque([root])
        while queue:
            res.append(None)
            for _ in range(len(queue)):
                node = queue.popleft()
                res[-1] = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return res
    # 1 dfs

    def rightSideView2(self, root: TreeNode) -> List[int]:
        res = []

        def dfs(root: TreeNode, level: int):
            if not root:
                return
            if len(res) == level:
                res.append(root.val)
            else:
                res[level] = root.val
            dfs(root.left, level+1)
            dfs(root.right, level+1)
        dfs(root, 0)
        return res

    # dfs 2020-04-22
    def rightSideView3(self, root: TreeNode) -> List[int]:
        res = []

        def _dfs(node: TreeNode, level: int):
            if not node:
                return
            if len(res) > level:
                res[level] = node.val
            else:
                res.append(node.val)
            _dfs(node.left, level + 1)
            _dfs(node.right, level + 1)
        _dfs(root, 0)
        return res


root = TreeNode(1)
root.left, root.right = TreeNode(2), TreeNode(3)
root.left.right = TreeNode(5)
root.right.right = TreeNode(4)
so = Solution()
print(so.rightSideView3(root))
