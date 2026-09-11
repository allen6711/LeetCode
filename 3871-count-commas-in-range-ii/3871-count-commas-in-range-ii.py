class Solution:
    def countCommas(self, n: int) -> int:
        # O(logn)
        # O(1)
        ans = 0
        threshold = 1000

        while threshold <= n:
            ans += n - threshold + 1
            threshold *= 1000
        
        return ans