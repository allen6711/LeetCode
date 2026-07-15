class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        # O(1)
        # O(1)
        return n
        
        # O(n)
        # O(1)
        sumOdd = 0
        sumEven = 0

        for i in range(n):
            sumOdd += 2 * i - 1
            sumEven += 2 * i
        
        return gcd(sumOdd, sumEven)