class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # O(n)
        # O(1)
        if len(nums) <= 2:
            return len(nums)
        
        write = 2

        for read in range(2, len(nums)):
            if nums[read] != nums[write - 2]:
                nums[write] = nums[read]
                write += 1
        
        return write