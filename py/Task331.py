class Solution:
    # recursion using stack
    def isValidSerialization(self, preorder: str) -> bool:
        q = preorder.split(',')
        q.reverse()

        def recursion() -> bool:
            if not q:
                return False
            if q.pop() == '#':
                return True
            else:
                return recursion() and recursion()

        return recursion() and not q

    # recursion(dfs) using array iteration
    def isValidSerialization2(self, preorder: str) -> bool:
        nodes = preorder.split(',')
        n = len(nodes)
        i = 0

        def dfs():
            nonlocal i
            if i == n:
                return False
            node = nodes[i]
            i += 1
            if node == '#':
                return True
            else:
                return dfs() and dfs()

        return dfs() and i == n

    # iteratrion
    def isValidSerialization3(self, preorder: str) -> bool:
        slots = 1
        for node in preorder.split(','):
            if not slots:
                return False
            slots -= 1
            if node != '#':
                slots += 2
        return not slots


preorder = "1,#"
so = Solution()
print(so.isValidSerialization3(preorder))
