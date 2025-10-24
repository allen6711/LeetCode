# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_bool, q_bool, lca_node = self.helper(root, p, q)

        return lca_node if p_bool and q_bool else None

    def helper(self, root, p, q):
        if root is None:
            return False, False, None
        
        left_p, left_q, left_node = self.helper(root.left, p, q)
        right_p, right_q, right_node = self.helper(root.right, p, q)

        p_bool = left_p or right_p or root is p
        q_bool = left_q or right_q or root is q

        if root is p or root is q:
            return p_bool, q_bool, root
        
        if left_node and right_node:
            return p_bool, q_bool, root

        if left_node:
            return p_bool, q_bool, left_node
        
        if right_node:
            return p_bool, q_bool, right_node
        
        return p_bool, q_bool, None


    #     p_bool, q_bool, lca_node = self.helper(root, p, q)

    #     return lca_node if p_bool and q_bool else None
    
    # def helper(self, root, p, q):
    #     if root is None:
    #         return False, False, None
        
    #     p_left, q_left, left_node = self.helper(root.left, p, q)
    #     p_right, q_right, right_node = self.helper(root.right, p, q)

    #     p_bool = p_left or p_right or root is p
    #     q_bool = q_left or q_right or root is q

    #     if root is p or root is q:
    #         return p_bool, q_bool, root

    #     if left_node and right_node:
    #         return p_bool, q_bool, root
        
    #     if left_node:
    #         return p_bool, q_bool, left_node
        
    #     if right_node:
    #         return p_bool, q_bool, right_node
        
    #     return p_bool, q_bool, None



    #     p_bool, q_bool, lca_node = self.helper(root, p, q)

    #     return lca_node if p_bool and q_bool else None
    
    # def helper(self, root, p, q):
    #     if root is None:
    #         return False, False, None
        
    #     p_left, q_left, left_node = self.helper(root.left, p, q)
    #     p_right, q_right, right_node = self.helper(root.right, p, q)

    #     p_bool = p_left or p_right or root is p
    #     q_bool = q_left or q_right or root is q

    #     if root is p or root is q:
    #         return p_bool, q_bool, root

    #     if left_node and right_node:
    #         return p_bool, q_bool, root
        
    #     if left_node:
    #         return p_bool, q_bool, left_node
        
    #     if right_node:
    #         return p_bool, q_bool, right_node
        
    #     return p_bool, q_bool, None

    #     p_bool, q_bool, lca_node = self.helper(root, p, q)

    #     return lca_node if p_bool and q_bool else None
    
    # def helper(self, root, p, q):
    #     if root is None:
    #         return False, False, None
        
    #     left_p, left_q, left_node = self.helper(root.left, p, q)
    #     right_p, right_q, right_node = self.helper(root.right, p, q)

    #     p_bool = left_p or right_p or root is p
    #     q_bool = left_q or right_q or root is q

    #     if root is p or root is q:
    #         return p_bool, q_bool, root
        
    #     if left_node is not None and right_node is not None:
    #         return p_bool, q_bool, root
        
    #     if left_node:
    #         return p_bool, q_bool, left_node
        
    #     if right_node:
    #         return p_bool, q_bool, right_node
        
    #     return p_bool, q_bool, None


        
    #     p_bool, q_bool, lca_node = self.helper(root, p, q)

    #     return lca_node if p_bool and q_bool else None
    
    # def helper(self, root, p, q):
    #     if root is None:
    #         return False, False, None
        
    #     p_left, q_left, left_node = self.helper(root.left, p, q)
    #     p_right, q_right, right_node = self.helper(root.right, p, q)

    #     p_bool = p_left or p_right or root is p
    #     q_bool = q_left or q_right or root is q

    #     if root is p or root is q:
    #         return p_bool, q_bool, root
        
    #     if left_node is not None and right_node is not None:
    #         return p_bool, q_bool, root

    #     if left_node:
    #         return p_bool, q_bool, left_node
        
    #     if right_node:
    #         return p_bool, q_bool, right_node
        
    #     return p_bool, q_bool, None

    #     p_bool, q_bool, LCA_node = self.helper(root, p, q)

    #     return LCA_node if p_bool and q_bool else None
    
    # def helper(self, root, p, q):
    #     if root is None:
    #         return False, False, None
        
    #     p_left, q_left, left_node = self.helper(root.left, p, q)
    #     p_right, q_right, right_node = self.helper(root.right, p, q)
        
    #     p_bool = p_left or p_right or root is p
    #     q_bool = q_left or q_right or root is q
        
    #     if root is p or root is q:
    #         return p_bool, q_bool, root
        
    #     if left_node is not None and right_node is not None:
    #         return p_bool, q_bool, root
        
    #     if left_node is not None:
    #         return p_bool, q_bool, left_node

    #     if right_node is not None:
    #         return p_bool, q_bool, right_node
        
    #     return p_bool, q_bool, None


    #     p_bool, q_bool, lca = self.helper(root, p, q)

    #     if p_bool and q_bool:
    #         return lca
        
    #     else:
    #         return None
    
    # def helper(self, node, p, q):
    #     if node is None:
    #         return False, False, None

    #     left_p, left_q, left_node = self.helper(node.left, p, q)
    #     right_p, right_q, right_node = self.helper(node.right, p, q)

    #     p_bool = left_p or right_p or node == p
    #     q_bool = left_q or right_q or node == q

    #     if node == p or node == q:
    #         return p_bool, q_bool, node
        
    #     if left_node is not None and right_node is not None:
    #         return p_bool, q_bool, node
        
    #     if left_node is not None:
    #         return p_bool, q_bool, left_node
        
    #     if right_node is not None:
    #         return p_bool, q_bool, right_node

    #     return p_bool, q_bool, None



    #     p_bool, q_bool, lca = self.helper(root, p, q)

    #     if p_bool and q_bool:
    #         return lca
        
    #     else:
    #         return None

    # def helper(self, root, p, q):
    #     if root is None:
    #         return False, False, None
        
    #     left_p, left_q, left_node = self.helper(root.left, p, q)
    #     right_p, right_q, right_node = self.helper(root.right, p, q)

    #     # p exists
    #     p_bool = left_p or right_p or root == p

    #     # q exists
    #     q_bool = left_q or right_q or root == q

    #     if root == p or root == q:
    #         return p_bool, q_bool, root

    #     if left_node is not None and right_node is not None:
    #         return p_bool, q_bool, root

    #     if left_node is not None:
    #         return p_bool, q_bool, left_node

    #     if right_node is not None:
    #         return p_bool, q_bool, right_node

    #     return p_bool, q_bool, None

