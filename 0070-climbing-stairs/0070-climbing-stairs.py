class Solution:
    def climbStairs(self, n: int) -> int:
        # O(n)
        # O(n)
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[n]
        # O(n)
        # O(1)
        # dp[0]
        prev2 = 1
        # dp[1]
        prev1 = 1
        for i in range(2, n + 1):
            cur = prev2 + prev1
            prev2 = prev1
            prev1 = cur
        
        return prev1