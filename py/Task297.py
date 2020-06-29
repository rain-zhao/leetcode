# Definition for a binary tree node.
from queue import SimpleQueue


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    # # bfs
    # def serialize(self, root):
    #     l = []
    #     q = SimpleQueue()
    #     q.put(root)
    #     while not q.empty():
    #         node = q.get()
    #         if not node:
    #             l.append('N')
    #             continue
    #         l.append(str(node.val))
    #         q.put(node.left)
    #         q.put(node.right)
    #     return ','.join(l)

    # # bfs
    # def deserialize(self, data):
    #     data = data.split(',')
    #     if not data or data[0] == 'N':
    #         return None
    #     root = TreeNode(int(data[0]))
    #     q = SimpleQueue()
    #     q.put(root)
    #     pos = 1
    #     while not q.empty():
    #         node = q.get()
    #         left = data[pos]
    #         pos += 1
    #         right = data[pos]
    #         pos += 1
    #         if left != 'N':
    #             node.left = TreeNode(int(left))
    #             q.put(node.left)
    #         if right != 'N':
    #             node.right = TreeNode(int(right))
    #             q.put(node.right)
    #     return root

    # dfs
    def serialize(self, root):
        def dfs(node: TreeNode) -> str:
            if not node:
                return 'N'
            return str(node.val) + ','+dfs(node.left)+','+dfs(node.right)
        return dfs(root)
        # l = []

        # def dfs(node: TreeNode):
        #     if not node:
        #         l.append('N')
        #         return
        #     l.append(str(node.val))
        #     dfs(node.left)
        #     dfs(node.right)
        # dfs(root)
        # return ','.join(l)

    # dfs

    def deserialize(self, data):
        data = data.split(',')
        it = iter(data)

        def dfs() -> TreeNode:
            val = next(it)
            if val == 'N':
                return None
            node = TreeNode(int(val))
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()


codec = Codec()
s = "1,2,N,N,3,4,N,N,5,N,N"
root = codec.deserialize(s)
s1 = codec.serialize(root)
print(s1)
