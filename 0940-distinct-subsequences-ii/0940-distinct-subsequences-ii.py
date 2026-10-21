class Solution:
    def distinctSubseqII(self, s: str) -> int:
        # O(n)
        # O(1)
        MOD = 10 ** 9 + 7
        last = [0] * 26
        total = 1

        for ch in s:
            idx = ord(ch) - ord('a')

            prev = total
            total = (2 * total - last[idx]) % MOD
            last[idx] = prev
        
        return (total - 1) % MOD
        # O(n)
        # O(n)
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