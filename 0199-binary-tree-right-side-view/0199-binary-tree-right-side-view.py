# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        from collections import deque
        if not root:
            return []
        q = deque([root])
        ans = []
        while q:
            size = len(q)
            for _ in range(size):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            ans.append(node.val)
        
        return ans

        
        # from collections import deque
        # if not root:
        #     return []
        
        # ans = []
        # q = deque([root])
        # while q:
        #     size = len(q)
        #     for i in range(size):
        #         node = q.popleft()
        #         # if i == size - 1:
        #         #     ans.append(node.val)
        #         if node.left:
        #             q.append(node.left)
        #         if node.right:
        #             q.append(node.right)
        #     ans.append(node.val)
        
        # return ans