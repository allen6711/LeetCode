"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        # dummy + tail
        if not root:
            return None
        level_start = root

        while level_start:
            dummy = Node(0)
            tail = dummy
            cur = level_start
            while cur:
                if cur.left:
                    tail.next = cur.left
                    tail = tail.next
                if cur.right:
                    tail.next = cur.right
                    tail = tail.next
                cur = cur.next
            level_start = dummy.next
        
        return root


        # # dummy + tail
        # if not root:
        #     return None
        
        # level_start = root
        # while level_start:
        #     dummy = Node(0)
        #     tail = dummy
        #     cur = level_start
        #     while cur:
        #         if cur.left:
        #             tail.next = cur.left
        #             tail = tail.next
        #         if cur.right:
        #             tail.next = cur.right
        #             tail = tail.next
        #         cur = cur.next
        #     level_start = dummy.next
        
        # return root
        # BFS
        # from collections import deque
        # if not root:
        #     return None
        
        # q = deque([root])
        # while q:
        #     size = len(q)
        #     prev = None
        #     for _ in range(size):
        #         node = q.popleft()
        #         if prev:
        #             prev.next = node
        #         prev = node
        #         if node.left:
        #             q.append(node.left)
        #         if node.right:
        #             q.append(node.right)
            
        #     prev.next = None
        
        # return root

        # BFS
        # if not root:
        #     return None
        # from collections import deque
        # q = deque([root])
        # while q:
        #     size = len(q)
        #     prev = None
        #     for _ in range(size):
        #         node = q.popleft()
        #         if prev:
        #             prev.next = node
        #         prev = node
        #         if node.left:
        #             q.append(node.left)
        #         if node.right:
        #             q.append(node.right)
        #     prev.next = None
        
        # return root
