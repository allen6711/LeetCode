class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # O(n)
        # O(n)
        num_set = set(nums)
        x = 1
        while x in num_set:
            x += 1
        return x
        # O(n)
        # O(1)
        n = len(nums)
        for i in range(n):
            while 1 <= nums[i] <= n:
                correct_idx = nums[i] - 1
                if nums[correct_idx] == nums[i]:
                    break
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
        
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        return n + 1
                
