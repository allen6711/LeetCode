# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less_dummy = ListNode(0)
        ge_dummy = ListNode(0)
        less_tail = less_dummy
        ge_tail = ge_dummy

        cur = head
        while cur:
            if cur.val < x:
                less_tail.next = cur
                less_tail = less_tail.next
            else:
                ge_tail.next = cur
                ge_tail = ge_tail.next
            cur = cur.next
        
        less_tail.next = ge_dummy.next
        ge_tail.next = None
        return less_dummy.next



        # O(n)
        # O(n)
        # if not head:
        #     return None
        # small = []
        # large = []
        # cur = head
        # while cur:
        #     if cur.val < x:
        #         small.append(cur)
        #     else:
        #         large.append(cur)
        #     cur = cur.next
        
        # arr = small + large
        
        # for i in range(len(arr) - 1):
        #     arr[i].next = arr[i + 1]
        
        # arr[-1].next = None

        # return arr[0]
        # O(n)
        # O(1)
        less_dummy = ListNode(0)
        ge_dummy = ListNode(0)
        less_tail = less_dummy
        ge_tail = ge_dummy

        cur = head
        while cur:
            # next_node = cur.next
            if cur.val < x:
                less_tail.next = cur
                less_tail = less_tail.next
            else:
                ge_tail.next = cur
                ge_tail = ge_tail.next

            cur = cur.next

        ge_tail.next = None
        less_tail.next = ge_dummy.next
        return less_dummy.next
