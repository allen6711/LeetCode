# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        from collections import deque
        if not root:
            return []
        q = deque([root])
        ans = []
        while q:
            size = len(q)
            level_total = 0
            for _ in range(size):
                node = q.popleft()
                level_total += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            ans.append(level_total / size)
        
        return ans


        
        # from collections import deque
        # if not root:
        #     return []
        # ans = []
        # q = deque([root])
        # while q:
        #     level_sum = 0
        #     size = len(q)

        #     for i in range(size):
        #         node = q.popleft()
        #         level_sum += node.val
                
        #         if node.left:
        #             q.append(node.left)
        #         if node.right:
        #             q.append(node.right)
            
        #     ans.append(level_sum / size)
        
        # return ans
        
        