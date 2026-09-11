class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        # k: consecutive numbers
        # x + (x + 1) + (x + 2) + ... + (x + k - 1)
        # sum = n = [(x + x + k - 1) * k] / 2
        # n = [(2x + k - 1) * k] / 2
        # [(2n / k) + 1 - k] = x
        # x = [(2n + k - k^2)] / k
        # x = [2n - k(k - 1)] / k
        # O(sqrt(n))    ->  k(k + 1) <= 2n
        # O(1)
        ans = 0 # x
        k = 1

        while k * (k - 1) // 2 < n:
            remain = n - k * (k - 1) // 2
            if remain % k == 0:
                ans += 1
            
            k += 1
        
        return ans