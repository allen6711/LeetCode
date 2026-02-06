class Solution:
    def findMin(self, nums: List[int]) -> int:
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            # Check the positions is at the peak's left or right
            if nums[mid] <= nums[-1]:
                end = mid
            else:
                start = mid
        
        return min(nums[start], nums[end])
        
        # if not nums:
        #     return -1

        # start, end = 0, len(nums) - 1

        # while start + 1 < end:
        #     mid = (start + end) // 2

        #     if nums[mid] <= nums[-1]:
        #         end = mid
            
        #     else:
        #         start = mid
        
        # # start may be less than end
        # return min(nums[start], nums[end])


        # if not nums:
        #     return -1
        
        # start, end = 0, len(nums) - 1

        # while start + 1 < end:
        #     mid = (start + end) // 2

        #     if nums[mid] <= nums[-1]:
        #         end = mid

        #     else:
        #         start = mid
        
        # return min(nums[start], nums[end])




        # if not nums:
        #     return -1
        
        # start, end = 0, len(nums) - 1

        # while start + 1 < end:
        #     mid = (start + end) // 2

        #     if nums[mid] <= nums[-1]:
        #         end = mid
            
        #     else:
        #         start = mid

        # return min(nums[start], nums[end])


        # left, right = 0, len(nums) - 1
        # index = -1

        # while left <= right:
        #     mid = (left + right) // 2
        #     if nums[mid] <= nums[-1]:
        #         index = mid
        #         right = mid - 1
        #     else:
        #         left = mid + 1
        # return nums[index]