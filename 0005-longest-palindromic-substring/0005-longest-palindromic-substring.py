class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_len = 0
        n = len(s)
        ans = ""
        def extand(left: int, right: int) -> str:
            nonlocal max_len, ans
            while left >= 0 and right < n and s[left] == s[right]:
                if len(s[left:right + 1]) > max_len:
                    ans = s[left:right + 1]
                    max_len = len(s[left: right + 1])
                
                left -= 1
                right += 1
        
        for i in range(n):
            extand(i, i)
            extand(i, i + 1)
        
        return ans

            













        res = ""
        n = len(s)

        def expand(left, right):
            nonlocal res

            while left >= 0 and right < n and s[left] == s[right]:
                if right - left + 1 > len(res):
                    res = s[left:right + 1]
                
                left -= 1
                right += 1
        
        for i in range(n):
            # odd-length palindrome
            expand()

        return res

















        n = len(s)
        dp = [[True] * n for _ in range(n)]
        max_length = 1
        start_index = 0

        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                dp[i][j] = False

                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    if max_length < j - i + 1:
                        start_index = i
                        max_length = j - i + 1
        
        return s[start_index: start_index + max_length]
