# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p1, p2 = l1, l2
        dummy = ListNode()
        prev = dummy
        carry = 0

        while p1 or p2 or carry:
            x = p1.val if p1 else 0
            y = p2.val if p2 else 0
            total = x + y + carry
            carry = total // 10
            remainder = total % 10
            prev.next = ListNode(remainder)
            prev = prev.next
            if p1:
                p1 = p1.next
            if p2:
                p2 = p2.next
        

        return dummy.next


        # p1, p2 = l1, l2
        # carry = 0
        # dummy = ListNode()
        # tail = dummy

        # while p1 or p2 or carry:
        #     x = p1.val if p1 else 0
        #     y = p2.val if p2 else 0
        #     total = x + y + carry
        #     carry = total // 10
        #     remainder = total % 10
        #     tail.next = ListNode(remainder)
        #     tail = tail.next

        #     if p1:
        #         p1 = p1.next
        #     if p2:
        #         p2 = p2.next

        # return dummy.next


        # p1, p2 = l1, l2
        # carry = 0
        # dummy = ListNode(0)
        # prev = dummy

        # while p1 or p2 or carry:
        #     x = p1.val if p1 else 0
        #     y = p2.val if p2 else 0
        #     total = x + y + carry
        #     carry = total // 10
        #     remain = total % 10

        #     prev.next = ListNode(remain)
        #     prev = prev.next

        #     if p1:
        #         p1 = p1.next

        #     if p2:
        #         p2 = p2.next
        
        # return dummy.next

        # dummy = ListNode(0)
        # cur = dummy
        # p1, p2 = l1, l2
        # carry = 0

        # while p1 or p2 or carry:
        #     x = p1.val if p1 else 0
        #     y = p2.val if p2 else 0
        #     total = x + y + carry
        #     carry = total // 10
        #     retain = total % 10
        #     cur.next = ListNode(retain)
        #     cur = cur.next

        #     if p1:
        #         p1 = p1.next
        #     if p2:
        #         p2 = p2.next
        
        # return dummy.next
        
        # dummy = ListNode(0)
        # tail = dummy
        # p1, p2 = l1, l2
        # carry = 0
        
        # while p1 or p2 or carry:
        #     x = p1.val if p1 else 0
        #     y = p2.val if p2 else 0
        #     total = x + y + carry
        #     carry = total // 10
        #     remain = total % 10
        #     tail.next = ListNode(remain)
        #     tail = tail.next
            
        #     if p1:
        #         p1 = p1.next
        #     if p2:
        #         p2 = p2.next
        
        # return dummy.next

        # dummy_head = ListNode()
        # carry, current = 0, dummy_head

        # while l1 or l2 or carry:
        #     sum = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
        #     carry, value = divmod(sum, 10)
        #     current.next = ListNode(value)
        #     current = current.next
        #     l1 = l1.next if l1 else None
        #     l2 = l2.next if l2 else None
        
        # return dummy_head.next