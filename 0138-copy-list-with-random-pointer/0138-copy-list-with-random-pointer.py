"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Node:
    def __init__(self, val=0, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        originToClone = {}
        # First traverse, clone all nodes
        cur = head
        while cur:
            if cur not in originToClone:
                originToClone[cur] = Node(cur.val)
            
            cur = cur.next
        # Second traverse, link all clone nodes
        cur = head
        while cur:
            if cur.next:
                originToClone[cur].next = originToClone[cur.next]
            if cur.random:
                originToClone[cur].random = originToClone[cur.random]
            
            cur = cur.next
        
        return originToClone.get(head)