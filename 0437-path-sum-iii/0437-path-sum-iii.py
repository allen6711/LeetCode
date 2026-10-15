# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> int:
        prefix_count = defaultdict(int)
        prefix_count[0] = 1

        def dfs(node, prefix):
            if not node:
                return 0
            
            prefix += node.val

            count = prefix_count[prefix - targetSum]

            prefix_count[prefix] += 1

            count += dfs(node.left, prefix)
            count += dfs(node.right, prefix)

            prefix_count[prefix] -= 1

            return count
        
        return dfs(root, 0)