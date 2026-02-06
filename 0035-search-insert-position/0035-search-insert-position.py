class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
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
        
        # edge cases        
        if target <= nums[0]:
            return 0
        if target > nums[-1]:
            return len(nums)
        
        return right
        
        















        # left, right = 0, len(nums)
        # while left < right:
        #     mid = (left + right) // 2
        #     if nums[mid] >= target:
        #         right = mid
        #     else:
        #         left = mid + 1
        
        # return left