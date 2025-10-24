# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        if root is None:
            return None

        if root in nodes:
            return root
        
        left_node = self.lowestCommonAncestor(root.left, nodes)
        right_node = self.lowestCommonAncestor(root.right, nodes)

        if left_node and right_node:
            return root
        
        if left_node:
            return left_node

        if right_node:
            return right_node
        
        return None

        # if root is None:
        #     return None
        
        # if root in nodes:
        #     return root
        
        # left_node = self.lowestCommonAncestor(root.left, nodes)
        # right_node = self.lowestCommonAncestor(root.right, nodes)

        # if left_node and right_node:
        #     return root
        
        # if left_node:
        #     return left_node
        
        # if right_node:
        #     return right_node
        
        # return None


        # if root is None:
        #     return None
        
        # if root in nodes:
        #     return root

        # left_node = self.lowestCommonAncestor(root.left, nodes)
        # right_node = self.lowestCommonAncestor(root.right, nodes)

        # if left_node and right_node:
        #     return root
        
        # if left_node:
        #     return left_node
        
        # if right_node:
        #     return right_node
        
        # return None
        