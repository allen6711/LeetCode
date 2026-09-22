class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0
        n = len(nums)
        for right in range(1, n):
            # We don't need to care the same pair
            if nums[left] != nums[right]:
                left += 1
                nums[left] = nums[right]
        
        return left + 1













        # O(n)
        # O(1)
        left = 0
        for right in range(1, len(nums)):
            if nums[right] != nums[left]:
                left += 1
                nums[left] = nums[right]
                
        return left + 1