
# Definition for a Node.


class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors


class Solution:

    map = {None: None}

    def cloneGraph(self, node: 'Node') -> 'Node':
        if node in self.dict:
            return self.dict[node]
        cpy = Node(node.val, [])
        self.dict[node] = cpy
        for neighbor in node.neighbors:
            cpy.neighbors.append(self.cloneGraph(neighbor))
        return cpy

    def cloneGraph2(self, node: 'Node') -> 'Node':
        map = {None: None}

        def cloneNode(node):
            if node in map:
                return map[node]
            newNode = Node(node.val, [])
            map[node] = newNode
            for neighbor in node.neighbors:
                newNode.neighbors.append(cloneNode(neighbor))
            return newNode
        return cloneNode(node)


so = Solution()
so.cloneGraph(None)
