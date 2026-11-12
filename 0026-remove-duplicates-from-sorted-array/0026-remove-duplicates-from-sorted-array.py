class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # O(n)
        # O(1)
        if not nums:
            return 0

        slow = 0
        for fast in range(1, len(nums)):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
        
        return slow + 1