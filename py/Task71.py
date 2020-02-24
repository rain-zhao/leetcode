class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for itm in path.split('/'):
            if itm in ('.',''):
                continue
            elif itm == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(itm)
        return '/'+'/'.join(stack)

solution = Solution()
path = "/a/../../b/../c//.//"
print(solution.simplifyPath(path))
