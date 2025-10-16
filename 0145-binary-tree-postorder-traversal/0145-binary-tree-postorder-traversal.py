# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Use stack to apply postorder traversal
        if root is None:
            return []

        stack = [root]
        postorder = []

        while stack:
            node = stack.pop()
            postorder.append(node.val)

            if node.left:
                stack.append(node.left)

            if node.right:
                stack.append(node.right)
        
        return postorder[::-1]










        # Use stack to apply postorder traversal
        # if root is None:
        #     return []

        # stack = [root]
        # postorder = []

        # while stack:
        #     node = stack.pop()
        #     postorder.append(node.val)
            
        #     if node.left:
        #         stack.append(node.left)

        #     if node.right:
        #         stack.append(node.right)
        
        # return postorder[::-1]