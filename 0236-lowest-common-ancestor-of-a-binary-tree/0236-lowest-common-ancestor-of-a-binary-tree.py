# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None

        if p is root or q is root:
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root
        
        return left if left else right

        # if root is None:
        #     return None
        
        # if root is p or root is q:
        #     return root
        
        # left_node = self.lowestCommonAncestor(root.left, p, q)
        # right_node = self.lowestCommonAncestor(root.right, p, q)

        # if left_node and right_node:
        #     return root
        
        # if left_node:
        #     return left_node

        # if right_node:
        #     return right_node

        # return None

        # if root is None:
        #     return None

        # if root is p or root is q:
        #     return root
        
        # left_node = self.lowestCommonAncestor(root.left, p, q)
        # right_node = self.lowestCommonAncestor(root.right, p, q)

        # if left_node is not None and right_node is not None:
        #     return root
        
        # if left_node:
        #     return left_node

        # if right_node:
        #     return right_node
        
        # return None

        # if root is None:
        #     return None
        
        # if root is p or root is q:
        #     return root
        
        # left_node = self.lowestCommonAncestor(root.left, p, q)
        # right_node = self.lowestCommonAncestor(root.right, p, q)

        # if left_node is not None and right_node is not None:
        #     return root
        
        # if left_node:
        #     return left_node

        # if right_node:
        #     return right_node
        
        # return None

        # if root is None:
        #     return None

        # if root is p or root is q:
        #     return root
        
        # left_node = self.lowestCommonAncestor(root.left, p, q)
        # right_node = self.lowestCommonAncestor(root.right, p, q)

        # if left_node is not None and right_node is not None:
        #     return root
        
        # if left_node:
        #     return left_node
        
        # if right_node:
        #     return right_node
        
        # return None


        # if root is None:
        #     return None
        
        # if root is p or root is q:
        #     return root
        
        # left_node = self.lowestCommonAncestor(root.left, p, q)
        # right_node = self.lowestCommonAncestor(root.right, p, q)

        # if left_node and right_node:
        #     return root
        
        # if left_node:
        #     return left_node

        # if right_node:
        #     return right_node
        
        # return None



        # if root is None:
        #     return None
        
        # if root is p or root is q:
        #     return root
        
        # left_node = self.lowestCommonAncestor(root.left, p, q)
        # right_node = self.lowestCommonAncestor(root.right, p, q)

        # if left_node and right_node:
        #     return root

        # if left_node:
        #     return left_node
        
        # if right_node:
        #     return right_node
        
        # return None

        # if root is None:
        #     return None
        
        # if root is p or root is q:
        #     return root

        # left_node = self.lowestCommonAncestor(root.left, p, q)
        # right_node = self.lowestCommonAncestor(root.right, p, q)

        # if left_node and right_node:
        #     return root
        
        # if left_node:
        #     return left_node
        
        # if right_node:
        #     return right_node
        

        # return None


        # if root is None:
        #     return None
        
        # if root is p or root is q:
        #     return root
        
        # left_node = self.lowestCommonAncestor(root.left, p, q)
        # right_node = self.lowestCommonAncestor(root.right, p, q)

        # if left_node and right_node:
        #     return root

        # if left_node:
        #     return left_node

        # if right_node:
        #     return right_node
        
        # return None


        # if root is None:
        #     return None
        
        # if root is p or root is q:
        #     return root
        
        # left_node = self.lowestCommonAncestor(root.left, p, q)
        # right_node = self.lowestCommonAncestor(root.right, p, q)

        # if left_node and not right_node:
        #     return left_node
        
        # if not left_node and right_node:
        #     return right_node
        
        # if left_node and right_node:
        #     return root
        
        # return None

        # if root is None:
        #     return None

        # if root is p or root is q:
        #     return root
        
        # left = self.lowestCommonAncestor(root.left, p, q)
        # right = self.lowestCommonAncestor(root.right, p, q)

        # if left is not None and right is not None:
        #     return root

        # if left is not None:
        #     return left

        # if right is not None:
        #     return right

        # return None

        # if root is None:
        #     return None
        
        # if root is p or root is q:
        #     return root
        
        # left = self.lowestCommonAncestor(root.left, p, q)
        # right = self.lowestCommonAncestor(root.right, p, q)

        # if left is not None and right is not None:
        #     return root
        
        # if left is not None:
        #     return left

        # if right is not None:
        #     return right


        # if root is None:
        #     return None
        
        # if root is p or root is q:
        #      return root
            
        # left = self.lowestCommonAncestor(root.left, p, q)
        # right = self.lowestCommonAncestor(root.right, p, q)

        # if left is not None and right is not None:
        #     return root
        
        # if left is not None:
        #     return left

        # if right is not None:
        #     return right

        # return None

        # if root is None:
        #     return None

        # if root is p or root is q:
        #      return root

        # left = self.lowestCommonAncestor(root.left, p, q)
        # right = self.lowestCommonAncestor(root.right, p, q)

        # if left is not None and right is not None:
        #     return root
        
        # if left is not None:
        #     return left

        # if right is not None:
        #     return right
        
        # return None


        
        # if root is None:
        #     return None

        # if root is p or root is q:
        #     return root
        
        # left = self.lowestCommonAncestor(root.left, p, q)
        # right = self.lowestCommonAncestor(root.right, p, q)

        # if left is not None and right is not None:
        #     return root
        
        # if left is not None:
        #     return left
        
        # if right is not None:
        #     return right
        
        # return None



        # # Base case
        # if root is None or root == p or root == q:
        #     return root

        # left = self.lowestCommonAncestor(root.left, p, q)
        # right = self.lowestCommonAncestor(root.right, p, q)

        # if left and right:
        #     return root
        
        # return left or right
