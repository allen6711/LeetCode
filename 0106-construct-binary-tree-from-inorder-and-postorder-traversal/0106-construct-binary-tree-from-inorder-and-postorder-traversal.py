# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        index = {}
        for i, val in enumerate(inorder):
            index[val] = i
        n = len(inorder)
        
        def dfs(inL, inR, postL, postR):
            if inL > inR:
                return None
            root_val = postorder[postR]
            root = TreeNode(root_val)
            k = index[root_val]
            left_size = k - inL
            root.left = dfs(inL, k - 1, postL, postL + left_size - 1)
            root.right = dfs(k + 1, inR, postL + left_size, postR - 1)

            return root
        
        return dfs(0, n - 1, 0, n - 1)









        # # Store value to index in dictionary
        # index = {}
        # for i, val in enumerate(inorder):
        #     index[val] = i
        # n = len(inorder)

        # # postorder: inf of root value
        # # inorder: pos of root and left size
        # def dfs(inL, inR, postL, postR):
        #     if postL > postR:
        #         return None
        #     root_val = postorder[postR]
        #     root = TreeNode(root_val)
        #     # post of root in inorder
        #     k = index[root_val]
        #     left_size = k - inL

        #     root.left = dfs(inL, k - 1, postL, postL + left_size - 1)
        #     root.right = dfs(k + 1, inR, postL + left_size, postR - 1)
            
        #     return root
        
        # return dfs(0, n - 1, 0, n - 1)

        # # Store value to index in dictionary
        # index = {}
        # for i, val in enumerate(inorder):
        #     index[val] = i
        
        # n = len(inorder)

        # def dfs(inL, inR, postL, postR):
        #     if inL > inR:
        #         return None
        #     root_val = postorder[postR]
        #     root = TreeNode(root_val)
        #     k = index[root_val]
        #     left_size = k - inL
        #     root.left = dfs(inL, k - 1, postL, postL + left_size - 1)
        #     root.right = dfs(k + 1, inR, postL + left_size, postR - 1)

        #     return root
        
        # return dfs(0, n - 1, 0, n - 1)

        # Store value: index
        # index = {}
        # for i, value in enumerate(inorder):
        #     index[value] = i
        
        # n = len(inorder)

        # def dfs(inL, inR, postL, postR):
        #     if inL > inR:
        #         return None
        #     root_val = postorder[postR]
        #     root = TreeNode(root_val)
        #     k = index[root_val]
        #     left_size = k - inL

        #     root.left = dfs(inL, k - 1, postL, postL + left_size - 1)
        #     root.right = dfs(k + 1, inR, postL + left_size, postR - 1)

        #     return root
        
        # return dfs(0, n - 1, 0, n - 1)
        