class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # O(n)
        # O(1)
        if not nums:
            return 0
        
        write = 1  # The first element must be unique
        for read in range(1, len(nums)):
            if nums[read] != nums[write - 1]:
                nums[write] = nums[read]
                write += 1
                
        return write