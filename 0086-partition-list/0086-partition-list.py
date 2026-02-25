# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # O(n)
        # O(n)
        if not head:
            return None
        small = []
        large = []
        cur = head
        while cur:
            if cur.val < x:
                small.append(cur)
            else:
                large.append(cur)
            cur = cur.next
        
        arr = small + large
        if not arr:
            return None
        
        for i in range(len(arr) - 1):
            arr[i].next = arr[i + 1]
        
        arr[-1].next = None

        return arr[0]