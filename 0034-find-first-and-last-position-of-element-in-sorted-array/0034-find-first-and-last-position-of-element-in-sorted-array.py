class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        
        first_position, last_position = -1, -1
        
        # first position:
        start, end = 0, len(nums) - 1
        
        while start + 1 < end:
            mid = (start + end) // 2

            if nums[mid] >= target:
                end = mid
            
            else:
                start = mid

        if nums[start] == target:
            first_position = start
        
        elif nums[end] == target:
            first_position = end

        # end position:
        start, end = 0, len(nums) - 1

        while start + 1 < end:
            mid = (start + end) // 2

            if nums[mid] <= target:
                start = mid
            
            else:
                end = mid
        
        if nums[end] == target:
            last_position = end

        elif nums[start] == target:
            last_position = start

        return [first_position, last_position]
        
        



        # if not nums:
        #     return [-1, -1]
        
        # first_position, last_position = -1, -1
        
        # # first position
        # start, end = 0, len(nums) - 1
        # while start + 1 < end:
        #     mid = (start + end) // 2

        #     if nums[mid] < target:
        #         start = mid
            
        #     elif nums[mid] > target:
        #         end = mid
            
        #     else:
        #         end = mid
        
        # if nums[start] == target:
        #     first_position = start
        
        # elif nums[end] == target:
        #     first_position = end
        
        # # last position
        # start, end = 0, len(nums) - 1
        # while start + 1 < end:
        #     mid = (start + end) // 2

        #     if nums[mid] < target:
        #         start = mid

        #     elif nums[mid] > target:
        #         end = mid
            
        #     else:
        #         start = mid
        
        # if nums[end] == target:
        #     last_position = end

        # elif nums[start] == target:
        #     last_position = start
        
        # return [first_position, last_position]



        # left, right = 0, len(nums) - 1
        # first_position, last_position = -1, -1
        # # first position
        # while left <= right:
        #     mid = (left + right) // 2
        #     if nums[mid] == target:
        #         first_position = mid
        #         right = mid - 1
        #     elif nums[mid] > target:
        #         right = mid - 1
        #     else:
        #         left = mid + 1
        
        # # last position
        # left, right = 0, len(nums) - 1
        # while left <= right:
        #     mid = (left + right) // 2
        #     if nums[mid] == target:
        #         last_position = mid
        #         left = mid + 1
        #     elif nums[mid] > target:
        #         right = mid - 1
        #     else:
        #         left = mid + 1
        # return (first_position, last_position)
