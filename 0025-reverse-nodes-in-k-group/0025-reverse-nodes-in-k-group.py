# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        group_prev = dummy

        while True:
            # Step 1: Find kth node
            kth = group_prev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next
            
            group_next = kth.next

            # Step 2: Reverse current group
            prev = group_next
            cur = group_prev.next
            while cur != group_next:
                next_node = cur.next
                cur.next = prev

                prev = cur
                cur = next_node
            
            # Step 3: Reconnect
            old_head = group_prev.next
            group_prev.next = kth
            group_prev = old_head