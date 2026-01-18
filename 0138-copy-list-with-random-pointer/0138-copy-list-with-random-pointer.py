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
        if not head:
            return None
        # Clone nodes
        cur = head
        while cur:
            next_node = cur.next
            copy = Node(cur.val)
            cur.next = copy
            copy.next = next_node
            cur = next_node
        # Clone random pointers
        cur = head
        while cur:
            copy = cur.next
            copy.random = cur.random.next if cur.random else None
            cur = copy.next
        # Split into 2 lists
        dummy = Node(0)
        copy_tail = dummy
        cur = head
        while cur:
            copy = cur.next
            copy_tail.next = copy
            copy_tail = copy
            cur = copy.next
        
        return dummy.next