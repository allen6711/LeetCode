# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        index = 1

        while reader.get(index) < target:
            index = index * 2
        
        start, end = 0, index
        
        while start + 1 < end:
            mid = (start + end) // 2

            if reader.get(mid) < target:
                start = mid
            
            else:
                end = mid
        
        if reader.get(start) == target:
            return start

        if reader.get(end) == target:
            return end
        
        return -1