# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        self.cur = 0

        def dfs(level: int) -> TreeNode:
            lastIdx = S.find('-', self.cur)
            if lastIdx == -1:
                lastIdx = len(S)
            root = TreeNode(int(S[self.cur:lastIdx]))
            self.cur = lastIdx
            if S[self.cur:self.cur+level+1] != '-' * (level + 1):
                return root
            self.cur += level + 1
            root.left = dfs(level + 1)
            if S[self.cur: self.cur+level+1] != '-' * (level + 1):
                return root
            self.cur += level + 1
            root.right = dfs(level + 1)
            return root

        root = dfs(0)
        return root


S = "1-401--349---90--88"
obj = Solution()
print(obj.recoverFromPreorder(S))
