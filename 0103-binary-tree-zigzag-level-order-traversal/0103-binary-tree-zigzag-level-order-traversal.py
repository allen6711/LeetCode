# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import deque
        if not root:
            return []
        q = deque([root])
        ans = []
        left_to_right = True

        while q:
            size = len(q)
            level_node = []
            for _ in range(size):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                
                level_node.append(node.val)
            
            if not left_to_right:
                level_node.reverse()
            
            left_to_right = not left_to_right
            ans.append(level_node)
        
        return ans











        if not root:
            return []
        ans = []
        q = deque([root])
        left_to_right = True
        while q:
            level = []
            size = len(q)
            for _ in range(size):
                node = q.popleft()
                level.append(node.val)
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            if not left_to_right:
                level.reverse()
            
            ans.append(level)
            left_to_right = not left_to_right
        
        return ans

        # if not root:
        #     return []
        
        # queue = deque([root])
        # result = []
        # left_to_right = True

        # while queue:
        #     level = []

        #     for _ in range(len(queue)):
        #         node = queue.popleft()
        #         level.append(node.val)

        #         if node.left:
        #             queue.append(node.left)
                    
        #         if node.right:
        #             queue.append(node.right)
                
        #     if not left_to_right:
        #         level.reverse()

        #     left_to_right = not left_to_right
        #     result.append(level)

        # return result


        # if root is None:
        #     return []
        
        # queue = deque([root])
        # result = []
        # left_to_right = True

        # while queue:
        #     level = []
        #     for _ in range(len(queue)):
        #         node = queue.popleft()
        #         level.append(node.val)
        #         if node.left:
        #             queue.append(node.left)
        #         if node.right:
        #             queue.append(node.right)
            
        #     if not left_to_right:
        #         level.reverse()

        #     result.append(level)
        #     left_to_right = not left_to_right

        # return result