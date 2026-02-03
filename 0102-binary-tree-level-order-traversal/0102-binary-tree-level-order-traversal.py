# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import deque
        if not root:
            return []
        
        q = deque([root])
        ans = []
        while q:
            size = len(q)
            level_node = []
            for _ in range(size):
                node = q.popleft()
                level_node.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            ans.append(level_node)
        
        return ans

        # if not root:
        #     return []
        # ans = []
        # q = deque([root])
        # while q:
        #     level = []
        #     size = len(q)
        #     for _ in range(size):
        #         node = q.popleft()
        #         level.append(node.val)
        #         if node.left:
        #             q.append(node.left)
        #         if node.right:
        #             q.append(node.right)
        #     ans.append(level)
        
        # return ans
        
        # if not root:
        #     return []

        # queue = deque([root])
        # result = []

        # while queue:
        #     level = []

        #     # We need one more for loop for level 
        #     for _ in range(len(queue)):
        #         node = queue.popleft()
        #         level.append(node.val)

        #         if node.left:
        #             queue.append(node.left)
                
        #         if node.right:
        #             queue.append(node.right)
            
        #     result.append(level)
        
        # return result
