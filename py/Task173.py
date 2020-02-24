# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from TreeNode import TreeNode


class BSTIterator:
    def __init__(self, root: TreeNode):
        self.arr = []
        self.cur = 0

        def dfs(root: TreeNode):
            if not root:
                return
            dfs(root.left)
            self.arr.append(root.val)
            dfs(root.right)
        dfs(root)
        return

    def next(self) -> int:
        self.cur += 1
        return self.arr[self.cur-1]

    def hasNext(self) -> bool:
        return self.cur < len(self.arr)


class BSTIterator2:
    def __init__(self, root: TreeNode):
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        root = self.stack.pop()
        node = root.right
        while node:
            self.stack.append(node)
            node = node.left
        return root.val

    def hasNext(self) -> bool:
        return self.stack


root = TreeNode(7)
root.left, root.right = TreeNode(3), TreeNode(15)
root.right.left, root.right.right = TreeNode(9), TreeNode(20)
iterator = BSTIterator(root)
iterator.next()    # 返回 3
iterator.next()    # 返回 7
iterator.hasNext()  # 返回 true
iterator.next()    # 返回 9
iterator.hasNext()  # 返回 true
iterator.next()    # 返回 15
iterator.hasNext()  # 返回 true
iterator.next()    # 返回 20
iterator.hasNext()  # 返回 false
