class Solution:
    def partition(self, s: str) -> list[list[str]]:
        ans = []
        path = []
        n = len(s)

        def isPalindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                
                left += 1
                right -= 1
            return True
        
        def backtrack(start):
            if start == n:
                ans.append(path[:])
                return
            
            for i in range(start, n):
                if isPalindrome(start, i):
                    path.append(s[start:i + 1])
                    backtrack(i + 1)
                    path.pop()
        
        backtrack(0)
        return ans