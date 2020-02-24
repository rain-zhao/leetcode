
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors



class Solution:

    dict = {}
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node in self.dict:
            return self.dict[node]
        cpy = Node(node.val,[])
        self.dict[node] = cpy
        for neighbor in node.neighbors:
            cpy.neighbors.append(self.cloneGraph(neighbor))
        return cpy

so = Solution()
so.cloneGraph(None)
