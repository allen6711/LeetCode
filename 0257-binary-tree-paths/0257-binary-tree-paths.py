# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        # Divide and Conquer
        if root is None:
            return []

        if root.left is None and root.right is None:
            return [str(root.val)]
        
        leftPaths = self.binaryTreePaths(root.left)
        rightPaths = self.binaryTreePaths(root.right)

        paths = []

        for path in leftPaths + rightPaths:
            paths.append(str(root.val) + '->' + path)
        
        return paths

        # # Traverse
        # if root is None:
    #         return []

    #     paths = []
    #     results = []
    #     self.dfs(root, [str(root.val)], results)

    #     return results

    # def dfs(self, node, paths, results):
    #     if node.left is None and node.right is None:
    #         results.append('->'.join(paths))
    #         return

    #     if node.left:
    #         paths.append(str(node.left.val))
    #         self.dfs(node.left, paths, results)
    #         paths.pop()

    #     if node.right:
    #         paths.append(str(node.right.val))
    #         self.dfs(node.right, paths, results)
    #         paths.pop()
                
