# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    # DFS + Flatten List
    # N: number of Integer
    # L: number if List
    # D: maximum of DFS Recursion Depth
    # O(N+L)
    # O(N+D)
    # def __init__(self, nestedList: [NestedInteger]):
    #     self.nums = []
    #     self.index = 0

    #     def dfs(nestedList):
    #         for item in nestedList: # O(N+L)
    #             if item.isInteger():
    #                 self.nums.append(item.getInteger())
    #             else:
    #                 dfs(item.getList())
        
    #     dfs(nestedList)

    # def next(self) -> int:
    #     num = self.nums[self.index]
    #     self.index += 1
    #     return num
    
    # def hasNext(self) -> bool:
    #      return self.index < len(self.nums)

    # Stack + Lazy Flatten
    def __init__(self, nestedList: [NestedInteger]):
        # Reverse so the leftmost item is on top
        self.stack = nestedList[::-1]
    
    def next(self) -> int:
        return self.stack.pop().getInteger()
    
    def hasNext(self) -> bool:
        while self.stack:
            if self.stack[-1].isInteger():
                return True
            
            # Expand the nested list
            nested_list = self.stack.pop().getList()

            for item in reversed(nested_list):
                self.stack.append(item)
        
        return False

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())