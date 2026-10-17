# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        
        # Step 1: Find middle
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse second half
        second = slow.next
        slow.next = None
        prev = None

        while second:
            next_node = second.next
            second.next = prev
            prev = second
            second = next_node
        
        # Step 3: Merge alternately
        first = head
        second = prev
        while second:
            first_next = first.next
            second_next = second.next

            first.next = second
            second.next = first_next
            
            first = first_next
            second = second_next
        
        return head