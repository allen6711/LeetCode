class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = self.twoPointer(s, 0, len(s) - 1)
        if left >= right:
            return True
        
        return self.is_palindrome(s, left + 1, right) or self.is_palindrome(s, left, right - 1)

    def is_palindrome(self, s, left, right):
        left, right = self.twoPointer(s, left, right)
        return left >= right

    def twoPointer(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return left, right
            
            left += 1
            right -= 1
        
        return left, right

        # def is_palindrome(left, right) -> bool:
        #     while left < right:
        #         if s[left] != s[right]:
        #             return False
        #         left += 1
        #         right -= 1
        #     return True
        
        # left, right = 0, len(s) - 1
        # while left < right:
        #     if s[left] != s[right]:
        #         return is_palindrome(left, right - 1) or is_palindrome(left + 1, right)
        #     left += 1
        #     right -= 1
        
        # return True