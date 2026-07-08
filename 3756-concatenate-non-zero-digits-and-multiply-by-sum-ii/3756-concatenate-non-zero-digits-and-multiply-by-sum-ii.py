class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10 ** 9 + 7
        n = len(s)

        sum_d = [0] * (n + 1)    # digit sum prefix
        cnt_nz = [0] * (n + 1)   # non-zero digit count prefix
        p = [0] * (n + 1)        # concatenated non-zero prefix
        pow10 = [1] * (n + 1)    # pow10 = 10^i % MOD

        for i in range(1, n + 1):
            pow10[i] = pow10[i - 1] * 10 % MOD
        
        for i, ch in enumerate(s):
            digit = int(ch)
            sum_d[i + 1] = sum_d[i] + digit
            cnt_nz[i + 1] = cnt_nz[i] + (1 if digit != 0 else 0)

            if digit != 0:
                p[i + 1] = (p[i] * 10 + digit) % MOD
            else:
                p[i + 1] = p[i]
        
        ans = []

        for l, r in queries:
            n0 = cnt_nz[r + 1] - cnt_nz[l]
            sd = sum_d[r + 1] - sum_d[l]

            x = (p[r + 1] - p[l] * pow10[n0]) % MOD

            ans.append((x * sd) % MOD)
        
        return ans
