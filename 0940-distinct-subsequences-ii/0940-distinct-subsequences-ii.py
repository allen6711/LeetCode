class Solution:
    def distinctSubseqII(self, s: str) -> int:
        n = len(s)
        MOD = 10 ** 9 + 7

        dp = [0] * (n + 1)
        dp[0] = 1
        last_seen = {}

        for i in range(1, n + 1):
            ch = s[i - 1]

            dp[i] = 2 * dp[i - 1]

            if ch in last_seen:
                j = last_seen[ch]
                dp[i] -= dp[j - 1]
            
            dp[i] %= MOD
            last_seen[ch] = i
        
        return (dp[n] - 1) % MOD