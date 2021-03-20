from typing import List


class Solution:
    # recursion
    def evalRPN(self, tokens: List[str]) -> int:
        def recur() -> int:
            top = tokens.pop()
            if top in '+-*/':
                p1, p2 = recur(), recur()
                if top == '+':
                    return p2 + p1
                elif top == '-':
                    return p2 - p1
                elif top == '*':
                    return p2 * p1
                elif top == '/':
                    return int(p2 / p1)
            return int(top)
        return recur()

    # iteration & stack
    def evalRPN2(self, tokens: List[str]) -> int:
        stack = []
        for op in tokens:
            if op in '+-*/':
                p1, p2 = stack.pop(), stack.pop()
                if op == '+':
                    stack.append(p2+p1)
                elif op == '-':
                    stack.append(p2-p1)
                elif op == '*':
                    stack.append(p2*p1)
                elif op == '/':
                    stack.append(int(p2/p1))
            else:
                stack.append(int(op))
        return stack[0]


tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
obj = Solution()
print(obj.evalRPN2(tokens))
