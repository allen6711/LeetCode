# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        index = {}
        for i, val in enumerate(inorder):
            index[val] = i
        
        n = len(inorder)

        def dfs(preL, preR, inL, inR):
            if preL > preR:
                return None
            root_val = preorder[preL]
            root = TreeNode(root_val)
            k = index[root_val]
            left_size = k - inL
            root.left = dfs(preL + 1, preL + left_size, inL, k - 1)
            root.right = dfs(preL + left_size + 1, preR, k + 1, inR)
            return root
        
        return dfs(0, n - 1, 0, n-1)
        

        # # Store value to index in dictionary
        # index = {}
        # for i, val in enumerate(inorder):
        #     index[val] = i
        
        # n = len(inorder)
        
        # # preorder->inf of root val
        # # inorder->inf of left size by root position
        # def dfs(preL, preR, inL, inR):
        #     if preL > preR:
        #         return None
        #     root_val = preorder[preL]
        #     root = TreeNode(root_val)
        #     # root position in inorder
        #     k = index[root_val]
        #     left_size = k - inL
        #     root.left = dfs(preL + 1, preL + left_size, inL, k - 1)
        #     root.right = dfs(preL + left_size + 1, preR, k + 1, inR)
        
        #     return root
        
        # return dfs(0, n - 1, 0, n - 1)


        # Store value to index in dictionary
        # index = {}
        # for i, val in enumerate(inorder):
        #     index[val] = i
        
        # n = len(inorder)
        
        # # preorder -> the value of root
        # # inorder -> find the position of root then split left and right
        
        # def dfs(preL, preR, inL, inR):
        #     if preL > preR:
        #         return None
        #     root_val = preorder[preL]
        #     root = TreeNode(root_val)
        #     # index of root in inorder
        #     k = index[root_val]
        #     left_size = k - inL

        #     root.left = dfs(preL + 1, preL + left_size, inL, k - 1)
        #     root.right = dfs(preL + left_size + 1, preR, k + 1, inR)

        #     return root
        
        # return dfs(0, n - 1, 0, n - 1)

        # Store value: index
        # index = {}
        # for i, val in enumerate(inorder):
        #     index[val] = i
        
        # n = len(preorder)

        # def dfs(preL, preR, inL, inR):
        #     if preL > preR:
        #         return None

        #     root_val = preorder[preL]
        #     root = TreeNode(root_val)
        #     k = index[root_val]
        #     left_size = k - inL

        #     root.left = dfs(preL + 1, preL + left_size, inL, k - 1)
        #     root.right = dfs(preL + left_size + 1, preR, k + 1, inR)


        #     return root

        # return dfs(0, n - 1, 0, n - 1)

        # value -> index in inorder
        # index = {}
        # for i, v in enumerate(inorder):
        #     index[v] = i
        
        # n = len(preorder)
        
        # def dfs(preL, preR, inL, inR):
        #     # build subtree from:
        #     # preorder[preL...preR], inorder[inL, inR]
        #     # interval is empty, same as inL > inR
        #     if preL > preR:
        #         return None

        #     root_val = preorder[preL]
        #     root = TreeNode(root_val)
        #     k = index[root_val]      # root position in inorder
        #     left_size = k - inL

        #     root.left = dfs(preL + 1, preL + left_size, inL, k - 1)
        #     root.right = dfs(preL + left_size + 1, preR, k + 1, inR)

        #     return root

        # return dfs(0, n - 1, 0, n - 1)


