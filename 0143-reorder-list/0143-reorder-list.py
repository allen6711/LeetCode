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
            return None
        # find the middle
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        # reverse
        prev = None
        cur = slow.next
        slow.next = None  # avoid cycle
        while cur:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
        
        # Merge two splits
        first, second = head, prev
        while second:
            first_next = first.next
            second_next = second.next

            first.next = second
            second.next = first_next

            first = first_next
            second = second_next












        # O(n)
        # O(n)
        # if not head or not head.next:
        #     return None
        
        # nodes = []
        # cur = head
        # while cur:
        #     nodes.append(cur)
        #     cur = cur.next
        
        # left, right = 0, len(nodes) - 1
        # while left < right:
        #     nodes[left].next = nodes[right]
        #     left += 1

        #     if left == right:
        #         break
            
        #     nodes[right].next = nodes[left]
        #     right -= 1

        # nodes[left].next = None
        # O(n)
        # O(1)
        # if not head or not head.next:
        #     return None
        # # 1. Find the end of the first half
        # slow, fast = head, head
        # while fast.next and fast.next.next:
        #     slow = slow.next
        #     fast = fast.next.next
            
        # # 2. Revese the second half
        # second = slow.next
        # slow.next = None  # Split the list into two halves
        # prev = None
        # cur = second
        # while cur:
        #     next_node = cur.next
        #     cur.next = prev
        #     prev = cur
        #     cur = next_node
        
        # # 3. Merge the two halves alternately
        # first, second = head, prev
        # while second:
        #     first_next = first.next
        #     second_next = second.next

        #     first.next = second
        #     second.next = first_next

        #     first = first_next
        #     second = second_next
        
