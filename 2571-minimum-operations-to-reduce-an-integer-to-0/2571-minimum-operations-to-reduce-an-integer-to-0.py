class Solution:
    def minOperations(self, n: int) -> int:
        # n += 2^i
        # n -= 2^i
        # In binary situation
        # Single 1, Consecutive 1
        # O(logn)
        # O(1)
        operations = 0

        while n > 0:
            if n % 2 == 0:
                n >>= 1
            
            # .....11
            elif n & 3 == 3:
                n += 1
                operations += 1
            
            else:
                n -= 1
                operations += 1
        
        return operations