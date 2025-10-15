# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Use stack to in-order traversal
        if root is None:
            return []
        
        dummy = TreeNode(0)
        dummy.right = root
        stack = [dummy]
        inorder = []

        while stack:
            node = stack.pop()

            if node.right:
                node = node.right
            
                while node:
                    stack.append(node)
                    node = node.left
                
            if stack:
                inorder.append(stack[-1].val)
        
        return inorder










        # result = []
        
        # while root:
        #     if root.left is None:
        #         result.append(root.val)
        #         root = root.right
            
        #     else:
        #         predecessor = root.left
        #         while predecessor.right and predecessor.right != root:
        #             predecessor = predecessor.right
                
        #         if predecessor.right is None:
        #             predecessor.right = root
        #             root = root.left
                
        #         else:
        #             result.append(root.val)
        #             predecessor.right = None
        #             root = root.right
        
        # return result