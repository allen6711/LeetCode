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
        prev = None
        def dfs(node):
            nonlocal prev
            if not node:
                return None
            dfs(node.right)
            dfs(node.left)
            node.left = None
            node.right = prev
            prev = node
        
        dfs(root)
            

        # prev = None
        # def dfs(node):
        #     nonlocal prev
        #     if not node:
        #         return None
        #     dfs(node.right)
        #     dfs(node.left)
        #     node.left = None
        #     node.right = prev
        #     prev = node
        
        # dfs(root)

        # prev = None
        # def dfs(node):
        #     nonlocal prev
        #     if not node:
        #         return None
        #     dfs(node.right)
        #     dfs(node.left)
            
        #     node.right = prev
        #     node.left = None
        #     prev = node
        
        # dfs(root)

        # prev = None
        # def dfs(node):
        #     nonlocal prev
        #     if not node:
        #         return
        #     dfs(node.right)
        #     dfs(node.left)
        #     node.right = prev
        #     node.left = None
        #     prev = node
        
        # dfs(root)


    #     self.helper(root)
    
    # def helper(self, root):
    #     if root is None:
    #         return None
        
    #     left_last = self.helper(root.left)
    #     right_last = self.helper(root.right)

    #     if left_last is not None:
    #         left_last.right = root.right
    #         root.right = root.left
    #         root.left = None
        
    #     if right_last is not None:
    #         return right_last
        
    #     if left_last is not None:
    #         return left_last
        
    #     return root

        
    #     self.helper(root)
    
    # def helper(self, node):
    #     if node is None:
    #         return None

    #     left_last = self.helper(node.left)
    #     right_last = self.helper(node.right)

    #     if left_last is not None:
    #         left_last.right = node.right
    #         node.right = node.left
    #         node.left = None
        
    #     if right_last is not None:
    #         return right_last

    #     if left_last is not None:
    #         return left_last

    #     return node


    #     self.helper(root)
    
    # def helper(self, node):
    #     if node is None: 
    #         return None

    #     left_last = self.helper(node.left)
    #     right_last = self.helper(node.right)

    #     if left_last is not None:
    #         left_last.right = node.right
    #         node.right = node.left
    #         node.left = None
        
    #     if right_last is not None:
    #         return right_last

    #     if left_last is not None:
    #         return left_last
        
    #     return node
        