# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        isBST, min, max = self.helper(root)

        return isBST
        
    def helper(self, node: Optional[TreeNode]):
        if node is None:
            return True, float('inf'), float('-inf')

        leftIsBST, leftMin, leftMax = self.helper(node.left)
        rightIsBST, rightMin, rightMax = self.helper(node.right)

        # Check left < root < right
        if not leftIsBST or not rightIsBST:
            return False, 0, 0
        
        if node.left and leftMax >= node.val:
            return False, 0, 0

        if node.right and rightMin <= node.val:
            return False, 0, 0
        
        minVal = min(leftMin, node.val)
        maxVal = max(rightMax, node.val)

        return True, minVal, maxVal




























    #     # in-order traversal
    #     self.preVal = None
    #     self.isBST = True
    #     self.validate(root)

    #     return self.isBST

    # def validate(self, root):
    #     if root is None:
    #         return
        
    #     self.validate(root.left)
    #     if self.preVal is not None and self.preVal >= root.val:
    #         self.isBST = False
    #         # Early termination if BST property is violated
    #         return

    #     self.preVal = root.val

    #     self.validate(root.right)


























        # def dfs(node: Optional[TreeNode], low: float, high: float) -> bool:
        #     if not node:
        #         return True
            
        #     if not (low < node.val < high):
        #         return False
            
        #     return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)

        # return dfs(root, float("-inf"), float("inf"))