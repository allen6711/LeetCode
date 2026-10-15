class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        # O(n)
        # O(n)
        n = len(nums)
        prefix_max = [float('-inf')] * n
        prefix_max[0] = nums[0]
        suffix_min = [float('inf')] * n
        suffix_min[-1] = nums[-1]
        for i in range(1, n):
            prefix_max[i] = max(prefix_max[i - 1], nums[i])
        for i in range(n - 2, -1, -1):
            suffix_min[i] = min(suffix_min[i + 1], nums[i])
        
        for i in range(n):
            if prefix_max[i] - suffix_min[i] <= k:
                return i
        
        return -1