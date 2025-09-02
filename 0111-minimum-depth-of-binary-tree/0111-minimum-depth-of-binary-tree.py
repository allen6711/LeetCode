# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:

        # BFS
        if root is None:
            return 0
        
        queue = deque([(root, 1)])

        while queue:
            node, depth = queue.popleft()
            if node.left is None and node.right is None:
                return depth
            
            if node.left:
                queue.append((node.left, depth + 1))

            if node.right:
                queue.append((node.right, depth + 1))
        
        return depth

        # DFS
        # if root is None:
        #     return 0
        
        # if root.left is None and root.right is not None:
        #     return 1 + self.minDepth(root.right)
        
        # if root.right is None and root.left is not None:
        #     return 1 + self.minDepth(root.left)
        
        # return 1 + min(self.minDepth(root.left), self.minDepth(root.right))