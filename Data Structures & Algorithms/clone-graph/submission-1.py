"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        m = {}        
        def clone(node):
            if node is None:
                return None
            if node.val in m:
                return m[node.val]
            root = Node(node.val)
            m[node.val] = root
            for nei in node.neighbors:
                root.neighbors.append(clone(nei))
            return root
        
        return clone(node)
