# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        prev = None
        cur = root
        count = 0
        
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            
            cur = stack.pop()
            count += 1
            if count == k:
                return cur.val
            prev = cur.val
            cur = cur.right








        if root is None:
            return []
        
        dummy = TreeNode(0)
        dummy.right = root
        stack = [dummy]

        for _ in range(k):
            node = stack.pop()

            if node.right:
                node = node.right

                while node:
                    stack.append(node)
                    node = node.left
            
            if not stack:
                return None
        
        return stack[-1].val








        # if root is None:
        #     return []
        
        # dummy = TreeNode(0)
        # dummy.right = root
        # stack = [dummy]

        # for _ in range(k):
        #     node = stack.pop()

        #     if node.right:
        #         node = node.right

        #         while node:
        #             stack.append(node)
        #             node = node.left
            
        #     if not stack:
        #         break
        
        # return stack[-1].val