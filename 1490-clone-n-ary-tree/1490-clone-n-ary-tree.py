"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        # O(n)
        # O(h)
        if not root:
            return None
        
        new_root = Node(root.val)
        for child in root.children:
            new_root.children.append(self.cloneTree(child))
        
        return new_root