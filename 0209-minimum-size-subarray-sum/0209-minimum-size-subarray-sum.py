class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # O(n)
        # O(1)
        n = len(nums)
        left = 0
        total = 0
        min_length = float('inf')
        for right in range(n):
            total += nums[right]
            while total >= target:
                min_length = min(min_length, right - left + 1)
                total -= nums[left]
                left += 1

        return 0 if min_length == float('inf') else min_length