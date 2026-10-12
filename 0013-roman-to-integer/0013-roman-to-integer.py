class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        ans = 0
        n = len(s)
        for i in range(n):
            if i < n - 1 and roman_dict[s[i]] < roman_dict[s[i + 1]]:
                ans -= roman_dict[s[i]]
            else:
                ans += roman_dict[s[i]]
            
        return ans















        # O(n)
        # O(1)
        values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
            }
        total = 0
        n = len(s)
        for i in range(n):
            if i < n - 1 and values[s[i]] < values[s[i + 1]]:
                total -= values[s[i]]
            else:
                total += values[s[i]]
        
        return total