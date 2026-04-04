"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Original Node -> New Node
        h = {}
        cur = head
        while cur:
            h[cur] = Node(cur.val)
            cur = cur.next
        
        cur = head
        while cur:
            node = h[cur]
            if cur.next:
                node.next = h[cur.next]
            else:
                node.next = None
            if cur.random:
                node.random = h[cur.random]
            else:
                node.random = None
            cur = cur.next
            
        if head:
            return h[head]
        else:
            return None