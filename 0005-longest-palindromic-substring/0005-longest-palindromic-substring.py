class Solution:
    def longestPalindrome(self, s: str) -> str:
        # DP
        #
        #
        n = len(s)
        # is dp[i][j] = s[i:j + 1] palindrome
        dp = [[False] * n for _ in range(n)]
        start = 0
        max_len = 1

        # Single character must be palindrom
        for i in range(n):
            dp[i][i] = True
        
        # length = substring
        for length in range(2, n + 1):
            for i in range(n - length + 1):  # i 最終會走到n-length (最後一個substring的位置)
                j = i + length - 1           # j 開始會從i + length - 1的地方開始
                if s[i] == s[j]:
                    if length <= 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                
                if dp[i][j] and length > max_len:
                    start = i
                    max_len = length
        
        return s[start:start + max_len]
        # O(n)
        # O(1)
        max_length = 0
        n = len(s)
        start = 0
        def expand(left: int, right: int):
            nonlocal max_length, start
            while left >= 0 and right < n and s[left] == s[right]:
                cur_length = right - left + 1
                if cur_length > max_length:
                    start = left
                    max_length = cur_length
                
                left -= 1
                right += 1

        for i in range(n):
            expand(i, i)
            expand(i, i + 1)
        
        return s[start:start + max_length]

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
            expand(i, i + 1)
        
        return ans