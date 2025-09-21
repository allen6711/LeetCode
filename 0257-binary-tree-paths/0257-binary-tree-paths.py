# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        # Traverse
        if root is None:
            return []

        results = []

        self.dfs(root, [str(root.val)], results)

        return results

    def dfs(self, node, path, results):
        if node.left is None and node.right is None:
            results.append('->'.join(path))
            return
        
        if node.left:
            path.append(str(node.left.val))
            self.dfs(node.left, path, results)
            path.pop()
        
        if node.right:
            path.append(str(node.right.val))
            self.dfs(node.right, path, results)
            path.pop()
        
        
