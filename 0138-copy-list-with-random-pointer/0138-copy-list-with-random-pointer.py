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
        
        old_to_new = {}
        cur = head
        # {A: A', B: B'. C: C'}
        while cur:
            old_to_new[cur] = Node(cur.val)
            cur = cur.next
        
        cur = head
        while cur:
            old_to_new[cur].next = old_to_new.get(cur.next)
            old_to_new[cur].random = old_to_new.get(cur.random)
            cur = cur.next
        
        return old_to_new[head]



        # Hash Map method
        # O(n)
        # O(n)
        # if not head:
        #     return None
        
        # old_to_new = {}
        # # Pass 1: copy every node
        # cur = head
        # while cur:
        #     old_to_new[cur] = Node(cur.val)
        #     cur = cur.next
        
        # # Pass 2: connect next and random
        # cur = head
        # while cur:
        #     old_to_new[cur].next = old_to_new.get(cur.next) # A->B, cur.next is B (在dict裡面link)
        #     old_to_new[cur].random = old_to_new.get(cur.random)
        #     cur = cur.next
        
        # return old_to_new[head]

        # if not head:
        #     return None

        # No Hash Map
        # O(n)
        # O(1)
        if not head:
            return None
        cur = head
        # Insert copied node after each original node
        # A->A'->B->B'->C->C'
        while cur:
            copy = Node(cur.val)
            copy.next = cur.next
            cur.next = copy
            cur = copy.next
        
        # Set random pointers
        cur = head
        while cur:
            copy = cur.next
            if cur.random:
                copy.random = cur.random.next
            
            cur = copy.next
        
        # Seperate original and copied lists
        cur = head
        copy_head = head.next
        while cur:
            copy = cur.next
            cur.next = copy.next

            if copy.next:
                copy.next = copy.next.next
            
            cur = cur.next
        
        return copy_head
        
        # if not head:
        #     return None
        # # Copy node
        # ## A -> B -> C
        # ## A -> A' -> B -> B' -> C -> C'
        # cur = head
        # while cur:
        #     copy = Node(cur.val)
        #     next_node = cur.next
        #     cur.next = copy
        #     copy.next = next_node
        #     cur = next_node
        # # Copy random
        # ## A -> C, A' -> C'
        # cur = head
        # while cur:
        #     copy = cur.next
        #     copy.random = cur.random.next if cur.random else None
        #     cur = copy.next
        # # Split into 2 lists
        # dummy = Node(0)
        # copy_tail = dummy
        # cur = head
        # while cur:
        #     copy = cur.next
        #     copy_tail.next = copy
        #     copy_tail = copy
        #     cur = copy.next
        
        # return dummy.next

        # # if not head:
        # #     return None
        # # # Clone node
        # # ## x -> y -> z
        # # ##   \> x'\>y'
        # # cur = head
        # # while cur:
        # #     copy = Node(cur.val)
        # #     next_node = cur.next
        # #     cur.next = copy
        # #     copy.next = next_node
        # #     cur = next_node
        # # # Clone random pointer
        # # cur = head
        # # while cur:
        # #     copy = cur.next
        # #     copy.random = cur.random.next if cur.random else None
        # #     cur = copy.next
        # # # Split into 2 lists
        # # dummy = Node(0)
        # # copy_tail = dummy
        # # cur = head
        # # while cur:
        # #     copy = cur.next
        # #     copy_tail.next = copy
        # #     copy_tail = copy
        # #     cur = copy.next
        
        # # return dummy.next

        # if not head:
        #     return None
        # # Clone nodes
        # cur = head
        # while cur:
        #     next_node = cur.next
        #     copy = Node(cur.val)
        #     cur.next = copy
        #     copy.next = next_node
        #     cur = next_node
        # # Clone random pointers
        # cur = head
        # while cur:
        #     copy = cur.next
        #     copy.random = cur.random.next if cur.random else None
        #     cur = copy.next
        # # Split into 2 lists
        # dummy = Node(0)
        # copy_tail = dummy
        # cur = head
        # while cur:
        #     copy = cur.next
        #     copy_tail.next = copy
        #     copy_tail = copy
        #     cur = copy.next
        
        # return dummy.next