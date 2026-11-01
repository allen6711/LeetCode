# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # DFS
        # O(H)
        # Auxiliary Space: O(H)
        # Total Space: O(H)
        def dfs(node, max_so_far):
            if node is None:
                return 0
            
            # Check whether the current node is good
            if node.val >= max_so_far:
                good = 1
            else:
                good = 0
            
            max_so_far = max(max_so_far, node.val)

            # Count good nodes in both subtrees
            left = dfs(node.left, max_so_far)
            right = dfs(node.right, max_so_far)

            return good + left + right
        
        return dfs(root, float('-inf'))

        # BFS
        # O(N)
        # Auxiliary Space: O(W)
        # Total Space: O(W)
        from collections import deque

        if root is None:
            return 0
        
        count = 0
        queue = deque([(root, float("-inf"))])

        while queue:
            node, max_so_far = queue.popleft()

            if node.val >= max_so_far:
                count += 1
               
            max_so_far = max(max_so_far, node.val)
            
            if node.left:
                queue.append((node.left, max_so_far))
            
            if node.right:
                queue.append((node.right, max_so_far))
        
        return count