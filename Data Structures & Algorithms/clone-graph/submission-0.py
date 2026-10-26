"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        reference = {}

        def dfs(node):
            if node in reference:
                return reference[node]

            copy = Node(node.val)
            # new node created here
            reference[node] = copy
            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor))
                # copying original node neighbors to the copy recursively
            return copy
        
        if node:
            return dfs(node)
        else:
            return None
        