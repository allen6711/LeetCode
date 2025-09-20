# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced, _ = self.validate(root)

        return balanced

    
    def validate(self, root):
        if root is None:
            return True, 0
        
        balanced, left_height = self.validate(root.left)
        if not balanced:
            return False, 0

        balanced, right_height = self.validate(root.right)
        if not balanced:
            return False, 0

        return abs(left_height - right_height) <= 1, max(left_height, right_height) + 1






















    #     balanced, _ = self.validate(root)

    #     return balanced

    # def validate(self, root):
    #     if root is None:
    #         return True, 0
        
    #     balanced, left_h = self.validate(root.left)
    #     if not balanced:
    #         # return balanced, left_h
    #                          # it's not important for the left height
    #         return balanced, 0

    #     balanced, right_h = self.validate(root.right)
    #     if not balanced:
    #         # return balanced, right_h
    #                          # it's not important for the left height
    #         return balanced, 0

    #     return abs(left_h - right_h) <= 1, max(left_h, right_h) + 1























        # def height(node: Optional[TreeNode]):
        #     if node is None:
        #         return 0
            
        #     lh = height(node.left)
        #     if lh == -1:
        #         return -1

        #     rh = height(node.right)
        #     if rh == -1:
        #         return -1

        #     if abs(lh - rh) > 1:
        #         return -1

        #     return 1 + max(lh, rh)
        
        # return height(root) != -1