# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # DFS
        # if not root:
        #     return None
        # root.left, root.right = root.right, root.left

        # self.invertTree(root.left)
        # self.invertTree(root.right)

        # return root
        # BFS
        from collections import deque
        if not root:
            return None

        q = deque([root])
        while q:
            node = q.popleft()
            node.left, node.right = node.right, node.left
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        
        return root










        # # DFS
        # if not root:
        #     return None
        # root.left, root.right = root.right, root.left
        # self.invertTree(root.left)
        # self.invertTree(root.right)
        
        # return root

        # # BFS
        # from collections import deque
        # if not root:
        #     return None
        # q = deque([root])
        # while q:
        #     node = q.popleft()
        #     node.left, node.right = node.right, node.left
        #     if node.left:    # None doesn't have .left and .right
        #         q.append(node.left)
        #     if node.right:
        #         q.append(node.right)
        
        # return root


        # # DFS
        # if not root:
        #     return None
        
        # root.left, root.right = root.right, root.left
        # self.invertTree(root.left)
        # self.invertTree(root.right)

        # return root
        # # BFS
        # from collections import deque
        # if not root:
        #     return None
        # q = deque([root])
        # while q:
        #     node = q.popleft()
        #     node.left, node.right = node.right, node.left
        #     if node.left:
        #         q.append(node.left)
        #     if node.right:
        #         q.append(node.right)
        
        # return root

        # # DFS
        # if root is None:
        #     return None
        
        # root.left, root.right = root.right, root.left
        # self.invertTree(root.left)
        # self.invertTree(root.right)

        # return root

        # # BFS
        # from collections import deque
        # q = deque([root])
        # while q:
        #     node = q.popleft()
        #     node.left, node.right = node.right, node.left
        #     if node.left:
        #         q.append(node.left)
        #     if node.right:
        #         q.append(node.right)
        
        # return root

        # DFS
        # if root is None:
        #     return None
        
        # root.left, root.right = root.right, root.left
        # self.invertTree(root.left)
        # self.invertTree(root.right)

        # return root

        # BFS
        # from collections import deque
        # if root is None:
        #     return None
        # q = deque([root])
        # while q:
        #     node = q.popleft()
        #     node.left, node.right = node.right, node.left
        #     if node.left:
        #         q.append(node.left)
        #     if node.right:
        #         q.append(node.right)
        
        # return root


        # BFS
        # if root is None:
        #     return root

        # queue = deque([root])

        # while queue:
        #     node = queue.popleft()
        #     node.left, node.right = node.right, node.left
        #     if node.left:
        #         queue.append(node.left)
        #     if node.right:
        #         queue.append(node.right)
        
        # return root

        # DFS
        # if root is None:
        #     return root
        
        # root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)

        # return root
                
            
