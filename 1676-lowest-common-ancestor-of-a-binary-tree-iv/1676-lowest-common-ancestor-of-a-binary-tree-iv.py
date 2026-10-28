# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        targets = set(nodes)

        def dfs(node):
            if node is None:
                return None
            
            if node in targets:
                return node
            
            left_node = dfs(node.left)
            right_node = dfs(node.right)

            if left_node and right_node:
                return node
            
            if left_node:
                return left_node
            
            if right_node:
                return right_node
        
        return dfs(root)