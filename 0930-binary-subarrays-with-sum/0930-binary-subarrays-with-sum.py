class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        # O(n)
        # O(n)
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
        # O(n)
        # O(1)
        # Sliding Window
        def atMost(target: int) -> int:
            if target < 0:
                return 0
            
            left = 0
            total = 0
            window_sum = 0
            for right in range(len(nums)):
                window_sum += nums[right]

                while window_sum > target:
                    window_sum -= nums[left]
                    left += 1
                
                total += right - left + 1
            
            return total
        
        return atMost(goal) - atMost(goal - 1)
