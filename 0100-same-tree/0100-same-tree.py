# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # DFS
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        if p.val != q.val:
            return False
        
        # return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        # BFS
        from collections import deque
        pq = deque([(p, q)])
        while pq:
            p, q = pq.popleft()
            if p is None and q is None:
                continue
            if p is None or q is None:
                return False
            if p.val != q.val:
                return False
            pq.append((p.left, q.left))
            pq.append((p.right, q.right))
        
        return True


        # DFS
        # if p is None and q is None:
        #     return True
        # if p is None or q is None:
        #     return False
        # if p.val != q.val:
        #     return False

        # return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        # BFS
        # from collections import deque
    
        # pq = deque([(p, q)])
        # while pq:
        #     p, q = pq.popleft()
        #     if p is None and q is None:
        #         continue
        #     if p is None or q is None:
        #         return False
        #     if p.val != q.val:
        #         return False
        #     pq.append((p.left, q.left))
        #     pq.append((p.right, q.right))

        # return True

        # DFS
        # if p is None and q is None:
        #     return True
        # if p is None or q is None:
        #     return False
        # if p.val != q.val:
        #     return False

        # return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        # BFS
        # from collections import deque
        # dq = deque([(p, q)])
        # while dq:
        #     a, b = dq.popleft()
        #     if a is None and b is None:
        #         continue
        #     if a is None or b is None:
        #         return False
        #     if a.val != b.val:
        #         return False
            
        #     dq.append((a.left, b.left))
        #     dq.append((a.right, b.right))
        
        # return True


        # if not p and not q:
        #     return True

        # if not p or not q:
        #     return False
        
        # queue = deque([(p, q)])

        # while queue:
        #     node_p, node_q = queue.popleft()

        #     if not node_p and not node_q:
        #         continue
            
        #     if not node_p or not node_q:
        #         return False
            
        #     if node_p.val != node_q.val:
        #         return False
            
        #     queue.append((node_p.left, node_q.left))
        #     queue.append((node_p.right, node_q.right))
        
        # return True
        # DFS
        # if not p and not q:
        #     return True
        
        # if not p or not q:
        #      return False
        
        # if p.val != q.val:
        #     return False
        
        # return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        # BFS
        # queue = deque([(p, q)])

        # while queue:
        #     root_p, root_q = queue.popleft()
            
        #     if not root_p and not root_q:
        #         continue
            
        #     if not root_p or not root_q:
        #         return False
            
        #     if root_p.val != root_q.val:
        #         return False
            
        #     queue.append((root_p.left, root_q.left))
        #     queue.append((root_p.right, root_q.right))
        
        # return True
            