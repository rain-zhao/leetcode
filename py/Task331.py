class Solution:
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


preorder = "9,#,#,1"
so = Solution()
print(so.isValidSerialization(preorder))
