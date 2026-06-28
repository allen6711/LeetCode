class Solution:
    def numberOfWays(self, numPeople: int) -> int:
        MOD = 10 ** 9 + 7
        pairs = numPeople // 2
        dp = [0] * (pairs + 1)

        dp[0] = 1

        for i in range(1, pairs + 1):
            for j in range(i):
                dp[i] += dp[j] * dp[i - j - 1]
                dp[i] %= MOD
        
        return dp[pairs]













        # O(n^2)
        # O(n)
        MOD = 10 ** 9 + 7
        pairs = numPeople // 2
        dp = [0] * (pairs + 1)

        dp[0] = 1

        for i in range(1, pairs + 1):
            for j in range(i):
                dp[i] += dp[j] * dp[i - 1 - j]
                dp[i] %= MOD
        
        return dp[pairs]