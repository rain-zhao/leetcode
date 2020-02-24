from typing import List
import re


class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        if not input:
            return []
        inputs = re.split(r'(\D)', input)

        # def cal(op1: int, op: str, op2: int) -> int:
        #     if op == '+':
        #         return op1+op2
        #     elif op == '-':
        #         return op1-op2
        #     else:
        #         return op1*op2

        def compute(inputs: List) -> List[int]:
            if len(inputs) == 1:
                return [int(inputs[0])]
            # res = []
            # for i in range(1, len(inputs), 2):
            #     res1 = compute(inputs[:i])
            #     op = inputs[i]
            #     res2 = compute(inputs[i+1:])
            #     res += [cal(op1, op, op2) for op1 in res1 for op2 in res2]
            # return res
            return [op1+op2 if inputs[i] == '+' else op1-op2 if inputs[i] == '-' else op1*op2
                    for i in range(1, len(inputs), 2)
                    for op1 in compute(inputs[:i])
                    for op2 in compute(inputs[i+1:])]
        return compute(inputs)


input = "2*3-4*5"
so = Solution()
print(so.diffWaysToCompute(input))
