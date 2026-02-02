# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def left_height(node):
            h = 0
            while node:
                h += 1
                node = node.left
            return h
        
        def right_height(node):
            h = 0
            while node:
                h += 1
                node = node.right
            return h

        def dfs(node):
            if not node:
                return 0
            
            lh = left_height(node)
            rh = right_height(node)

            if lh == rh:
                return 2 ** lh - 1
            
            return 1 + dfs(node.left) + dfs(node.right)
        
        return dfs(root)


        # def left_height(node):
        #     h = 0
        #     while node:
        #         h += 1
        #         node = node.left
        #     return h
        # def right_height(node):
        #     h = 0
        #     while node:
        #         h += 1
        #         node = node.right
        #     return h

        
        # def dfs(node):
        #     if not node:
        #         return 0
            
        #     hl = left_height(node.left)
        #     hr = right_height(node.right)
        #     if hl == hr:
        #         return 2 ** hl - 1
            
        #     return 1 + dfs(node.left) + dfs(node.right)
        
        # return dfs(root)

        