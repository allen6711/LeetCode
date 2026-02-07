class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return -1
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] <= nums[-1]:
                right = mid
            else:
                left = mid
        
        return min(nums[left], nums[right])
















        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[mid] <= nums[-1]:
                right = mid
            else:
                left = mid
        
        return min(nums[left], nums[right])