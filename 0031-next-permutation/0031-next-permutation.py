class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        # Find the first nums[i] < nums[i + 1]
        i = n - 2

        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        
        # Find the pivot
        if i >= 0:
            j = n - 1

            # Find the first right num > nums[i]
            while nums[j] <= nums[i]:
                j -= 1
            
            nums[i], nums[j] = nums[j], nums[i]
        
        # Reverse suffix
        left, right = i + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        
        return nums