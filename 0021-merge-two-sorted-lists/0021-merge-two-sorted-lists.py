# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        p1, p2 = list1, list2
        cur = dummy
        while p1 and p2:
            if p1.val < p2.val:
                cur.next = p1
                p1 = p1.next
            else:
                cur.next = p2
                p2 = p2.next
            
            cur = cur.next
        
        if p1:
            cur.next = p1
        if p2:
            cur.next = p2
        

        return dummy.next






        # O(m+n)
        # O(1)
        dummy = ListNode(0)
        cur = dummy
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next

            cur = cur.next
        
        if list1:
            cur.next = list1
        
        if list2:
            cur.next = list2
        
        return dummy.next