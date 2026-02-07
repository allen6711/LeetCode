class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [self.firstPosition(nums, target), self.lastPosition(nums, target)]
    
    def firstPosition(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid
        if nums[left] == target:
            return left
        if nums[right] == target:
            return right

        return -1
    def lastPosition(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] <= target:
                left = mid
            else:
                right = mid
        if nums[right] == target:
            return right
        if nums[left] == target:
            return left

        return -1
        

















    #     if not nums:
    #         return [-1, -1]

    #     return [self.firstPosition(nums, target), self.lastPosition(nums, target)]
    
    # def firstPosition(self, nums: List[int], target: int) -> int:
    #     start, end = 0, len(nums) - 1
    #     while start + 1 < end:
    #         mid = (start + end) // 2
    #         if nums[mid] >= target:
    #             end = mid
    #         else:
    #             start = mid
    #     if nums[start] == target:
    #         return start
    #     if nums[end] == target:
    #         return end
        
    #     return -1

    # def lastPosition(self, nums: List[int], target: int) -> int:
    #     start, end = 0, len(nums) - 1
    #     while start + 1 < end:
    #         mid = (start + end) // 2
    #         if nums[mid] <= target:
    #             start = mid
    #         else:
    #             end = mid
    #     if nums[end] == target:
    #         return end
    #     if nums[start] == target:
    #         return start

    #     return -1
    



        # if not nums:
        #     return [-1, -1]
        # left, right = 0, len(nums)
        # while left < right:
        #     mid = (left + right) // 2
        #     if nums[mid] >= target:
        #         right = mid
        #     else:
        #         left = mid + 1
        
        # l = left

        # left, right = 0, len(nums)
        # while left < right:
        #     mid = (left + right) // 2
        #     if nums[mid] <= target:
        #         left = mid + 1
        #     else:
        #         right = mid
        
        # r = left - 1

        # # nums = [1, 3, 5], target = 10
        # # left = 3
        # if l == len(nums) or nums[l] != target:
        #     return [-1, -1]
        
        # return [l, r]

        
        # first_position, last_position = -1, -1
        
        # # first position:
        # start, end = 0, len(nums) - 1
        
        # while start + 1 < end:
        #     mid = (start + end) // 2

        #     if nums[mid] >= target:
        #         end = mid
            
        #     else:
        #         start = mid

        # if nums[start] == target:
        #     first_position = start
        
        # elif nums[end] == target:
        #     first_position = end

        # # end position:
        # start, end = 0, len(nums) - 1

        # while start + 1 < end:
        #     mid = (start + end) // 2

        #     if nums[mid] <= target:
        #         start = mid
            
        #     else:
        #         end = mid
        
        # if nums[end] == target:
        #     last_position = end

        # elif nums[start] == target:
        #     last_position = start

        # return [first_position, last_position]
        
        



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
