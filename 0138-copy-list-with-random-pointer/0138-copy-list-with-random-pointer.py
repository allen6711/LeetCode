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
        # 1. Clone and interleave
        cur = head
        while cur:
            copy = Node(cur.val)
            next_node = cur.next
            cur.next = copy
            copy.next = next_node
            cur = next_node
        # 2. Assign random for clone nodes
        cur = head
        while cur:
            copy = cur.next
            copy.random = cur.random.next if cur.random else None
            cur = copy.next
        # 3. Split into two lists
        cur = head
        dummy = Node(0)
        copy_tail = dummy
        while cur:
            copy = cur.next
            next_node = copy.next

            copy_tail.next = copy
            copy_tail = copy
            
            cur.next = next_node
            cur = next_node
        
        return dummy.next

        # if not head:
        #     return None
        
        # # 1. Clone and interleave
        # cur = head
        # while cur:
        #     next_node = cur.next
        #     copy = Node(cur.val)
        #     cur.next = copy
        #     copy.next = next_node
        #     cur = next_node
        # # 2. Assign random for clone nodes
        # cur = head
        # while cur:
        #     copy = cur.next
        #     copy.random = cur.random.next if cur.random else None
        #     cur = copy.next
        # # 3. Split into two lists
        # dummy = Node(0)
        # copy_tail = dummy
        # cur = head
        # while cur:
        #     copy = cur.next
        #     next_node = copy.next

        #     copy_tail.next = copy
        #     copy_tail = copy
            
        #     cur.next = next_node
        #     cur = next_node
        
        # return dummy.next
        
        # if not head:
        #     return None
        # # 1. Clone nodes and interleave
        # cur = head
        # while cur:
        #     next_node = cur.next
        #     copy = Node(cur.val)
        #     cur.next = copy
        #     copy.next = next_node
        #     cur = next_node
        # # 2. Assign random for clones
        # cur = head
        # while cur:
        #     copy = cur.next
        #     copy.random = cur.random.next if cur.random else None
        #     cur = copy.next
        # # 3. Split into two lists
        # dummy = Node(0)
        # copy_tail = dummy
        # cur = head
        # while cur:
        #     copy = cur.next
        #     next_node = copy.next

        #     copy_tail.next = copy
        #     copy_tail = copy

        #     cur.next = next_node
        #     cur = next_node
        
        # return dummy.next

        # if not head:
        #     return None
        # # 1. Interleave copied nodes with original nodes
        # cur = head
        # while cur:
        #     next_node = cur.next
        #     copy = Node(cur.val)
        #     cur.next = copy
        #     copy.next = next_node
        #     cur = next_node
        # # 2. Assign random pointers for the copied nodes
        # cur = head
        # while cur:
        #     copy = cur.next
        #     copy.random = cur.random.next if cur.random else None
        #     cur = copy.next
        # # 3. Separate the interleaved list into original and copied lists
        # dummy = Node(0)
        # copy_tail = dummy
        # cur = head
        # while cur:
        #     # A'
        #     copy = cur.next
        #     # B
        #     next_node = copy.next

        #     copy_tail.next = copy
        #     copy_tail = copy
        #     # A to B
        #     cur.next = next_node
        #     cur = next_node
        
        # return dummy.next