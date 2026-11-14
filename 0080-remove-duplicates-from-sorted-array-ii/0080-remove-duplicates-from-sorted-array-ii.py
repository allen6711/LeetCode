class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Intuitive approach, but with more code.
        # O(n)
        # O(1)
        slow, fast = 0, 0
        n = len(nums)
        limit = 0
        while fast < n:
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
            elif slow < fast and limit < 2:
                slow += 1
                nums[slow] = nums[fast]
            
            fast += 1
            limit += 1
            if fast < n and nums[fast] != nums[fast - 1]:
                limit = 0
        
        return slow + 1
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