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
        ans = []
        q = deque([root])
        while q:
            level_sum = 0.0
            size = len(q)
            for i in range(size):
                node = q.popleft()
                level_sum += node.val
                if i == size - 1:
                    level_sum /= size
                    ans.append(level_sum)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        
        return ans
        
        