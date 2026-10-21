class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # O(n)
        # O(n)
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
        cur = nums[0]
        ans = nums[0]
        for i in range(1, n):
            cur = max(nums[i], cur + nums[i])
            ans = max(ans, cur)
        
        return ans