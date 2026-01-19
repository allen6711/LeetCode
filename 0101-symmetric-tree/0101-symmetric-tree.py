# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.isMirror(root.left, root.right)
    
    def isMirror(self, a: Optoinal[TreeNode], b: Optioinal[TreeNode]) -> bool:
        if a is None and b is None:
            return True
        if a is None or b is None:
            return False
        if a.val != b.val:
            return False
        
        return self.isMirror(a.left, b.right) and self.isMirror(a.right, b.left)

        # if not root:
        #     return True
        
        # queue = deque([(root.left, root.right)])
        
        # while queue:
        #     root_l, root_r = queue.popleft()

        #     if not root_l and not root_r:
        #         continue
            
        #     if not root_l or not root_r:
        #         return False
            
        #     if root_l.val != root_r.val:
        #         return False
            
        #     queue.append((root_l.left, root_r.right))
        #     queue.append((root_l.right, root_r.left))      

        # return True
        
        # DFS
        # def isMirror(a: Optional[TreeNode], b: Optional[TreeNode]) -> bool:
        #     if not a and not b:
        #         return True
        #     if not a or not b:
        #         return False
        #     if a.val != b.val:
        #         return False
            
        #     return isMirror(a.left, b.right) and isMirror(a.right, b.left)
        
        # if not root:
        #     return True
        
        # return isMirror(root.left, root.right)


        # BFS
        # if not root:
        #      return True

        # queue = deque([(root.left, root.right)])

        # while queue:
        #     root_l, root_r = queue.popleft()
        #     if not root_l and not root_r:
        #         continue
        #     if not root_l or not root_r:
        #         return False
        #     if root_l.val != root_r.val:
        #         return False

        #     queue.append((root_l.left, root_r.right))
        #     queue.append((root_l.right, root_r.left))
        
        # return True