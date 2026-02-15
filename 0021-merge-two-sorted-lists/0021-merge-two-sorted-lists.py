# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        prev = dummy
        p1, p2 = list1, list2
        while p1 and p2:
            if p1.val <= p2.val:
                prev.next = p1
                p1 = p1.next
            else:
                prev.next = p2
                p2 = p2.next
            prev = prev.next
        
        prev.next = p1 if p1 else p2

        return dummy.next



        # dummy = ListNode(0)
        # tail = dummy
        # p1, p2 = list1, list2

        # while p1 and p2:
        #     if p1.val <= p2.val:
        #         tail.next = p1
        #         p1 = p1.next
        #     else:
        #         tail.next = p2
        #         p2 = p2.next
            
        #     tail = tail.next
        
        # tail.next = p1 if p1 else p2
    
        # return dummy.next

        # dummy = ListNode()
        # prev = dummy
        # p1, p2 = list1, list2
        # while p1 and p2:
        #     if p1.val <= p2.val:
        #         prev.next = p1
        #         p1 = p1.next
        #     else:
        #         prev.next = p2
        #         p2 = p2.next
            
        #     prev = prev.next
        
        # prev.next = p1 if p1 else p2

        # return dummy.next


        # dummy = ListNode(0)
        # tail = dummy
        # p1, p2 = list1, list2
        # while p1 and p2:
        #     if p1.val <= p2.val:
        #         tail.next = p1
        #         p1 = p1.next
        #     else:
        #         tail.next = p2
        #         p2 = p2.next

        #     tail = tail.next
        
        # tail.next = p1 if p1 else p2

        # return dummy.next

        # dummy = ListNode()
        # tail = dummy
        # p1, p2 = list1, list2

        # while p1 and p2:
        #     if p1.val <= p2.val:
        #         tail.next = p1
        #         p1 = p1.next
        #     else:
        #         tail.next = p2
        #         p2 = p2.next

        #     tail = tail.next

        # tail.next = p1 if p1 else p2

        # return dummy.next

        # dummy = ListNode()
        # tail = dummy
        # p1, p2 = list1, list2

        # while p1 and p2:
        #     if p1.val <= p2.val:
        #         tail.next = p1
        #         p1 = p1.next
        #     else:
        #         tail.next = p2
        #         p2 = p2.next

        #     tail = tail.next
        
        # tail.next = p1 if p1 else p2

        # return dummy.next

        # dummy = ListNode()
        # tail = dummy
        # point1, point2 = list1, list2

        # while point1 and point2:
        #     if point1.val <= point2.val:
        #         tail.next = point1
        #         point1 = point1.next
            
        #     else:
        #         tail.next = point2
        #         point2 = point2.next
            
        #     tail = tail.next
        
        # tail.next = point1 if point1 else point2

        # return dummy.next