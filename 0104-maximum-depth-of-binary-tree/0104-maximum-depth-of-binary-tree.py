# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# from typing import Optional
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # O(n)
        # O(h)
        # DFS
        if not root:
            return 0
        
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return 1 + max(left, right)
        # O(n)
        # O(w)
        # w: maximum number of nodes at any level of the tree
        # BFS
        from collections import deque
        if not root:
            return 0
        dq = deque([root])
        count = 0
        while dq:
            for _ in range(len(dq)):
                node = dq.popleft()
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            
            depth += 1
        
        return depth