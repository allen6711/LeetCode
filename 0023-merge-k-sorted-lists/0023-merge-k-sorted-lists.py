# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # O(nlogn)
        # O(n)
        vals = []
        for head in lists:
            while head:
                vals.append(head.val)
                head = head.next
        
        vals.sort()
        dummy = ListNode(0)
        cur = dummy
        for val in vals:
            cur.next = ListNode(val)
            cur = cur.next
        
        return dummy.next
        

















        heap = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))
        
        dummy = ListNode(0)
        tail = dummy

        while heap:
            _, i, node = heapq.heappop(heap)
            tail.next = node
            tail = tail.next
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
        
        # Prevent unexpected leftover links if the input lists are not well-formed
        tail.next = None
        
        return dummy.next
