# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # O(nlogn)
        # O(n)
        # vals = []
        # for head in lists:
        #     while head:
        #         vals.append(head.val)
        #         head = head.next
        
        # vals.sort()
        # dummy = ListNode(0)
        # cur = dummy
        # for val in vals:
        #     cur.next = ListNode(val)
        #     cur = cur.next
        
        # return dummy.next
        # O(nlogk)
        # O(k)
        heap = []
        counter = 0 # tie-breaker to avoid comparing ListNode objects

        for node in lists:
            if node:
                heapq.heappush(heap, (node.val, counter, node))
                counter += 1
        
        dummy = ListNode(0)
        cur = dummy

        while heap:
            val, _, node = heapq.heappop(heap)
            # Append the smallest node to the result
            cur.next = node
            cur = cur.next

            if node.next:
                heapq.heappush(heap, (node.next.val, counter, node.next))
                counter += 1

        # Ensure the final tail points to None (good hygiene)
        cur.next = None

        return dummy.next