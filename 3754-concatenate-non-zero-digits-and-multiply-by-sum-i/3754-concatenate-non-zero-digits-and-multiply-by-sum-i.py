class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x = 0
        digit_sum = 0
        for num in str(n):
            digit = int(num)
            digit_sum += digit
            if digit != 0:
                x = x * 10 + digit
            
        return x * digit_sum














        # O(n)
        # O(n)
        x = 0
        digit_sum = 0

        for ch in str(n):
            digit = int(ch)
            digit_sum += digit

            if digit != 0:
                x = x * 10 + digit
        
        return x * digit_sum
