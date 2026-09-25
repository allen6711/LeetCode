class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        # Max from left: prefix max
        # Min form right: suffix min
        # O(n)
        # O(n)
        # suffix_min[i] = min(nums[i:])
        n = len(nums)
        suffix_min = [0] * n
        suffix_min[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            suffix_min[i] = min(nums[i], suffix_min[i + 1])
        
        prefix_max = nums[0]

        for i in range(n):
            prefix_max = max(prefix_max, nums[i])

            if prefix_max - suffix_min[i] <= k:
                return i
        
        return -1
        # O(n^2)
        # O(1)
        n = len(nums)
        smallest = float('inf')
        for i in range(n):
            if max(nums[0:i + 1]) - min(nums[i: n]) <= k:
                smallest = min(smallest, i)
        
        return smallest if smallest != float('inf') else -1