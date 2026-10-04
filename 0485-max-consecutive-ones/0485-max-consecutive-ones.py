class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # O(n)
        # O(1)
        left = 0
        n = len(nums)
        max_count = 0
        for right in range(n):
            if nums[right] == 1:
                max_count = max(max_count, right - left + 1)
            else:
                left = right + 1
        
        return max_count
        # O(n)
        # O(1)
        count = 0
        count_max = 0
        for num in nums:
            if num == 1:
                count += 1
            else:
                count = 0
            count_max = max(count_max, count)
            
        return count_max