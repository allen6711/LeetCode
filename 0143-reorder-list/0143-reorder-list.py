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
        # Find the middle by two pointers
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Reverse the second list
        prev = None
        cur = slow.next
        slow.next = None
        while cur:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
        # Merge two halves
        first = head
        second = prev
        while second:
            temp1 = first.next
            temp2 = second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2










        # if not head or not head.next:
        #     return
        
        # # Find the middle
        # slow, fast = head, head
        # while fast and fast.next:
        #     slow = slow.next
        #     fast = fast.next.next

        # # Reverse Secound half
        # prev = None
        # cur = slow.next
        # slow.next = None
        # while cur:
        #     next_node = cur.next
        #     cur.next = prev
        #     prev = cur
        #     cur = next_node

        # second = prev  # Second head
        # first = head   # First head
        
        # # Merge two halves
        # while second:
        #     temp1 = first.next
        #     temp2 = second.next
        #     first.next = second
        #     second.next = temp1
        #     first = temp1
        #     second = temp2

        # if not head or not head.next:
        #     return 

        # # Find middle (slow will be at mid)
        # slow, fast = head, head
        # while fast and fast.next:
        #     slow = slow.next
        #     fast = fast.next.next
        
        # # Reverse second half
        # prev = None
        # cur = slow.next
        # slow.next = None  # cut the list into two halves

        # while cur:
        #     next_node = cur.next
        #     cur.next = prev
        #     prev = cur
        #     cur = next_node
        # second = prev  # head of reversed second half
        # first = head

        # # Merge two halves
        # while second:
        #     temp1 = first.next
        #     temp2 = second.next

        #     first.next = second
        #     second.next = temp1

        #     first = temp1
        #     second = temp2
        
