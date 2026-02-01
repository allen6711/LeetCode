# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# from typing import Optional
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # DFS
        if not root:
            return 0
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

        # BFS
        from collections import deque
        if not root:
            return 0
        q = deque([root])
        depth = 0
        while q:
            size = len(q)
            for _ in range(size):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            depth += 1
        
        return depth










        # # DFS
        # if root is None:
        #     return 0
        
        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        # # BFS
        # from collections import deque
        # if root is None:
        #     return 0
        # q = deque([root])
        # depth = 0
        # while q:
        #     size = len(q)
        #     for _ in range(size):
        #         node = q.popleft()
        #         if node.left:
        #             q.append(node.left)
        #         if node.right:
        #             q.append(node.right)
        #     depth += 1
        
        # return depth

        # DFS
        # if root is None:
        #     return 0
        
        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

        # # BFS
        # from collections import deque
        # if root is None:
        #     return 0

        # q = deque([root])
        # depth = 0
        # while q:
        #     for _ in range(len(q)):
        #         node = q.popleft()
        #         if node.left:
        #             q.append(node.left)
        #         if node.right:
        #             q.append(node.right)

        #     depth += 1
        
        # return depth










        # # DFS
        # if root is None:
        #     return 0
        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

        # # BFS
        # from collections import deque
        # if root is None:
        #     return 0
        # q = deque([root])
        # depth = 0
        # while q:
        #     for _ in range(len(q)):
        #         node = q.popleft()
        #         if node.left:
        #             q.append(node.left)
        #         if node.right:
        #             q.append(node.right)

        #     depth += 1

        # return depth


        # # DFS
        # if root is None:
        #     return 0
        
        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        
        # # BFS
        # from collections import deque
        # if root is None:
        #     return 0
        # q = deque([root])
        # depth = 0
        # while q:
        #     level_size = len(q)
        #     for _ in range(level_size):
        #         node = q.popleft()
        #         if node.left:
        #             q.append(node.left)
        #         if node.right:
        #             q.append(node.right)
        #     depth += 1
        # return depth

        # Divide and Conquer
        # if root is None:
        #     return 0
        
        # left_h = self.maxDepth(root.left)
        # right_h = self.maxDepth(root.right)

        # return 1 + max(left_h, right_h)
        

        # DFS
        # if root is None:
        #     return 0

        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))






















    #     if root is None:
    #         return 0

    #     return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
