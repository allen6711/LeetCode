# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        p1, p2 = headA, headB
        while p1 != p2:
            p1 = p1.next if p1 else headB
            p2 = p2.next if p2 else headA
        
        return p1








        # O(m + n)
        # O(m)
        # visited = set()
        # cur = headA
        # while cur:
        #     visited.add(cur)
        #     cur = cur.next
        
        # cur = headB
        # while cur:
        #     if cur in visited:
        #         return cur
        #     cur = cur.next
        
        # return None
        # O(m + n)
        # O(1)
        pA, pB = headA, headB
        
        while pA is not pB:
            pA = pA.next if pA else headB
            pB = pB.next if pB else headA
        
        return pA
