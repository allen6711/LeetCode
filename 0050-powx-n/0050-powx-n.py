class Solution:
    def myPow(self, x: float, n: int) -> float:
        # O(log|n|)
        # O(1)
        negative = n < 0
        n = abs(n)

        ans = 1.0

        while n > 0:
            if n % 2 == 1:
                ans *= x
            
            x *= x
            n //= 2
        
        return 1 / ans if negative else ans
            