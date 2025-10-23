"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        parent_set = set()
        curr = p

        while curr:
            parent_set.add(curr)
            curr = curr.parent
        
        curr = q

        while curr:
            if curr in parent_set:
                return curr
            curr = curr.parent
        
        return None








        # parent_set = set()
        # curr = p

        # while curr is not None:
        #     parent_set.add(curr)
        #     curr = curr.parent
        
        # curr = q

        # while curr is not None:
        #     if curr in parent_set:
        #         return curr
            
        #     curr = curr.parent
        
        # return None

        # parent_set = set()

        # curr = p

        # while curr is not None:
        #     parent_set.add(curr)
        #     curr = curr.parent
        
        # curr = q

        # while curr is not None:
        #     if curr in parent_set:
        #         return curr

        #     curr = curr.parent
        
        # return None