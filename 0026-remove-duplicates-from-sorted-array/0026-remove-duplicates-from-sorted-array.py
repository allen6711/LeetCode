class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:












        # O(n)
        # O(1)
        left = 0
        for right in range(1, len(nums)):
            if nums[right] != nums[left]:
                left += 1
                nums[left] = nums[right]
                
        return left + 1