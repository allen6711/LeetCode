class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        prefixsum_dict = {0: 1}
        prefixsum = 0
        ans = 0
        for num in nums:
            prefixsum += num
            if prefixsum - goal in prefixsum_dict:
                ans += prefixsum_dict[prefixsum - goal]
            
            prefixsum_dict[prefixsum] = prefixsum_dict.get(prefixsum, 0) + 1
        
        return ans