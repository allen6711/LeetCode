# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.preVal = None
        self.isBST = True
        self.validate(root)

        return self.isBST

    def validate(self, root):
        if root is None:
            return
        
        self.validate(root.left)
        if self.preVal is not None and self.preVal >= root.val:
            self.isBST = False
            # Early termination if BST property is violated
            return

        self.preVal = root.val

        self.validate(root.right)


























        # def dfs(node: Optional[TreeNode], low: float, high: float) -> bool:
        #     if not node:
        #         return True
            
        #     if not (low < node.val < high):
        #         return False
            
        #     return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)

        # return dfs(root, float("-inf"), float("inf"))