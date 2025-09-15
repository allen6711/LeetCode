# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        peak_index = self.findPeak(mountainArr)
        left_index, right_index = float('inf'), float('inf')
        print(peak_index)
        
        # left side:
        start, end = 0, peak_index

        while start + 1 < end:
            mid = (start + end) // 2

            if mountainArr.get(mid) <= target:
                start = mid
            
            else:
                end = mid
        
        if mountainArr.get(end) == target:
            left_index = end

        if mountainArr.get(start) == target:
            left_index = start
    
        # right side:
        start, end = peak_index, mountainArr.length() - 1

        while start + 1 < end:
            mid = (start + end) // 2

            if mountainArr.get(mid) <= target:
                end = mid

            else:
                start = mid
        
        if mountainArr.get(start) == target:
            right_index = start

        if mountainArr.get(end) == target:
            right_index = end
        
        return -1 if left_index == float('inf') and right_index == float('inf') else min(left_index, right_index)
        
    def findPeak(self, mountainArr) -> int:
        start, end = 0, mountainArr.length() - 1

        while start + 1 < end:
            mid = (start + end) // 2

            if mountainArr.get(mid) > mountainArr.get(mid + 1):
                end = mid
            
            elif mountainArr.get(mid) > mountainArr.get(mid - 1):
                start = mid
            
            else:
                return mid
        
        if mountainArr.get(start) > mountainArr.get(end):
            return start
        
        else:
            return end
    