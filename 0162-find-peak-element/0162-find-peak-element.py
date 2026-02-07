class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] < nums[mid + 1]:
                left = mid
            else:
                right = mid
        
        # peak at nums[0] or nums[-1]
        if nums[left] > nums[right]:
            return left
        else:
            return right

        # if not nums:
        #     return -1
        
        # start, end = 0, len(nums) - 1

        # while start + 1 < end:
        #     mid = (start + end) // 2

        #     # left side of peak
        #     if nums[mid - 1] < nums[mid]:
        #         start = mid
            
        #     elif nums[mid] < nums[mid - 1]:
        #         end = mid
            
        #     # elif nums[mid - 1] < nums[mid] < nums[mid + 1]:
        #     #     return mid
        #     else:
        #         return mid
        
        # if nums[start] > nums[end]:
        #     return start
        
        # else:
        #     return end

        # return -1





        # if not nums:
        #     return -1
        
        # start, end = 0, len(nums) - 1

        # while start + 1 < end:
        #     mid = (start + end) // 2

        #     if nums[mid - 1] < nums[mid]:
        #         start = mid
            
        #     elif nums[mid - 1] > nums[mid]:
        #         end = mid
            
        #     else:
        #         return mid
        
        # if nums[start] > nums[end]:
        #     return start
        
        # else:
        #     return end
        
        # return -1



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