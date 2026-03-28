class Solution:
    def intToRoman(self, num: int) -> str:
        # O(1)
        # O(1)
        values = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4, 1
        ]
        symbols = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV", "I"
        ]
        result = []
        
        n = len(values)
        for i in range(n):
            while num >= values[i]:
                result.append(symbols[i])
                num -= values[i]
        
        return "".join(result)