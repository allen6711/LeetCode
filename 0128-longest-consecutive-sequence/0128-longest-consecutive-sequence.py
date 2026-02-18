class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # O(n)
        # O(n)
        s = set(nums)
        best = 0
        for num in s:
            if num - 1 in s:
                continue    # not a sequence start
            num2 = num
            while num2 in s:
                num2 += 1
            
            best = max(best, num2 - num)  # length
            
        return best