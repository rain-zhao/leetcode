# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from typing import List
from TreeNode import TreeNode


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder:
            return None
        rootVal = postorder[-1]
        root = TreeNode(rootVal)
        for i, val in enumerate(inorder):
            if val == rootVal:
                root.left = self.buildTree(inorder[:i], postorder[:i])
                root.right = self.buildTree(inorder[i+1:], postorder[i:-1])
        return root

    def buildTree2(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def build(beg1: int, end1: int, beg2: int, end2: int) -> TreeNode:
            if beg1 == end1:
                return None
            rootVal = postorder[end2-1]
            root = TreeNode(rootVal)

            for shift in range(end1-beg1):
                if inorder[shift+beg1] == rootVal:
                    root.left = build(beg1, beg1+shift, beg2, beg2+shift)
                    root.right = build(beg1+shift+1, end1, beg2+shift, end2-1)
            return root

        return build(0, len(inorder), 0, len(postorder))

    def buildTree3(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        self.last = len(postorder)-1
        map = {val: idx for idx, val in enumerate(inorder)}
        a = 1
        def build(beg: int, end: int) -> TreeNode:
            a = a+1
            if beg == end:
                return None
            val = postorder[self.last]
            self.last -= 1
            root = TreeNode(val)
            root.right = build(map[val]+1, end)
            root.left = build(beg, map[val])
            return root

        return build(0, len(inorder))
