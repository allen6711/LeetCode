# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.helper(root)
    
    def helper(self, node):
        if node is None: 
            return None

        left_last = self.helper(node.left)
        right_last = self.helper(node.right)

        if left_last is not None:
            left_last.right = node.right
            node.right = node.left
            node.left = None
        
        if right_last is not None:
            return right_last

        if left_last is not None:
            return left_last
        
        return node
        