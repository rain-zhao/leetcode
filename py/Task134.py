from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        delta = [0]
        n = len(gas)
        for g, c in zip(gas, cost):
            delta.append(delta[-1]+g-c)
        if delta[-1] < 0:
            return -1
        # 最小idx的下一位
        minIdx, minVal = 0, delta[-1]
        for i in range(1, n):
            if delta[i] < minVal:
                minIdx, minVal = i, delta[i]
        return minIdx


gas = [5]
cost = [4]
obj = Solution()
print(obj.canCompleteCircuit(gas, cost))
