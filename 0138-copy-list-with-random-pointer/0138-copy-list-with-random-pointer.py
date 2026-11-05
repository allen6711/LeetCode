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
        # O(n)
        # O(n)
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

        # Interweaving
        # O(n)
        # O(1)
        if not head:
            return None
        # Insert cloned nodes after original nodes
        cur = head
        while cur:
            # A->A'->B->B'->C->C'
            copy = Node(cur.val)
            copy.next = cur.next
            cur.next = copy
            cur = copy.next
        # Set random pointers for cloned nodes
        cur = head
        while cur:
            copy = cur.next

            if cur.random:
                copy.random = cur.random.next
            
            cur = copy.next
        # Separate original and cloned lists
        cur = head
        copy_head = head.next

        while cur:
            copy = cur.next
            cur.next = copy.next

            if copy.next:
                copy.next = copy.next.next
            
            cur = cur.next
        
        return copy_head