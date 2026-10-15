class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        prefix_count = defaultdict(int)
        prefix_count[0] = 1
        prefixsum = 0
        ans = 0
        for num in nums:
            prefixsum += num
            if prefixsum - goal in prefix_count:
                ans += prefix_count[prefixsum - goal]
            prefix_count[prefixsum] += 1
        
        return ans