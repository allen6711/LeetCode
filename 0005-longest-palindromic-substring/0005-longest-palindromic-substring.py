class Solution:
    def longestPalindrome(self, s: str) -> str:
        # O(n)
        # O(1)
        # max_len = 0
        # n = len(s)
        # start = 0
        # def expand(left: int, right: int)
        # O(n)
        # O(n)
        max_len = 0
        n = len(s)
        ans = ""
        def expand(left: int, right: int):
            nonlocal max_len, ans
            while left >= 0 and right < n and s[left] == s[right]:
                cur_length = right - left + 1
                if cur_length > max_len:
                    ans = s[left:right + 1]
                    max_len = cur_length
                
                left -= 1
                right += 1
        
        for i in range(n):
            # Odd
            expand(i, i)
            # Even
            extand(i, i + 1)
        
        return ans