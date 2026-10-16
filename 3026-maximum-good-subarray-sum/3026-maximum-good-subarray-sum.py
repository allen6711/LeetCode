class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        # O(n)
        # O(n)
        min_prefix = {}
        prefix = 0
        ans = float('-inf')

        for num in nums:
            prefix += num
            if num + k in min_prefix:
                ans = max(ans, prefix - min_prefix[num + k])
            if num - k in min_prefix:
                ans = max(ans, prefix - min_prefix[num - k])
            
            min_prefix[num] = min(min_prefix.get(num, float('inf')), prefix - num)
        
        return 0 if ans == float('-inf') else ans