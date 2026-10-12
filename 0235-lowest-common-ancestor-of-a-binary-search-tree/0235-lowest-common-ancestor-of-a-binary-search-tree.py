# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # O(h)
        # O(1)
        # Irerative BST Search
        # while root:
        #     if p.val < root.val and q.val < root.val:
        #         root = root.left

        #     elif p.val > root.val and q.val > root.val:
        #         root= root.right

        #     else:
        #         return root
        # O(h)
        # O(h)
        # DFS
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root