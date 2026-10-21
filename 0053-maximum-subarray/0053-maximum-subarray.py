class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        cur = nums[0]
        ans = nums[0]
        for i in range(1, n):
            cur = max(nums[i], cur + nums[i])
            ans = max(ans, cur)
        
        return ans
            





        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        ans = dp[0]

        for i in range(1, n):
            dp[i] = max(nums[i], dp[i - 1] + nums[i])
            ans = max(ans, dp[i])
        
        return ans
















        # O(n)
        # O(1)
        n = len(nums)
        curr_max = nums[0]
        max_sum = nums[0]
        for i in range(1, n):
            curr_max = max(nums[i], curr_max + nums[i])
            max_sum = max(max_sum, curr_max)
        return max_sum
        # O(n)
        # O(n)
        n = len(nums)
        dp = [0] * n
        # dp[i]: sum of nums to nums[i]
        dp[0] = nums[0]
        for i in range(1, n):
            dp[i] = max(nums[i], dp[i - 1] + nums[i])
        
        return max(dp)
        
        
        # O(n^2)
        # O(1)
        max_sum = nums[0]
        n = len(nums)
        for i in range(n):
            total = 0
            for j in range(i, n):
                total += nums[j]
                if total > max_sum:
                    max_sum = total
                    
        return max_sum
        