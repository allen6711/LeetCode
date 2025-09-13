class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if not nums:
            return -1
        
        start, end = 0, len(nums) - 1

        while start + 1 < end:
            mid = (start + end) // 2

            if nums[mid - 1] < nums[mid]:
                start = mid
            
            elif nums[mid - 1] > nums[mid]:
                end = mid
            
            else:
                return mid
        
        if nums[start] > nums[end]:
            return start
        
        else:
            return end
        
        return -1
















        # if not nums:
        #     return -1
        
        # start, end = 0, len(nums) - 1

        # while start + 1 < end:
        #     mid = (start + end) // 2

        #     # Peak is on the right
        #     if nums[mid] < nums[mid + 1]:
        #         start = mid
            
        #     # Peak is on the left
        #     elif nums[mid] < nums[mid - 1]:
        #         end = mid
            
        #     # nums[mid] >= nums[mid + 1] and nums[mid] <= nums[mid - 1] -> peak
        #     else:
        #         return mid
        
        # #   start peak(end)
        # #   peak(start) end
        # if nums[start] > nums[end]:
        #     return start
        
        # else:
        #     return end



        # start, end = 0, len(nums) - 1
        # while start < end:
        #     mid = (start + end) // 2
        #     if nums[mid] > nums[mid + 1]:
        #         end = mid
        #     else:
        #         start = mid + 1

        # return start