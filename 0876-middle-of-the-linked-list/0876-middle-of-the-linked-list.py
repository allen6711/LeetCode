# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # O(n)
        # O(1)
        # length = 0
        # cur = head
        # while cur:
        #     cur = cur.next
        #     length += 1
        
        # cur = head
        # for _ in range(length // 2):
        #     cur = cur.next
        
        # return cur
        # O(n)
        # O(1)
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow