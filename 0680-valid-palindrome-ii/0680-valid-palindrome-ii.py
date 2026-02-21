class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return self.is_pal(s, left + 1, right) or self.is_pal(s, left, right - 1)
        
        return True

    def is_pal(self, s: str, left: int, right: int) -> bool:
        while left < right:
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        
        return True
            



    #     left, right = 0, len(s) - 1

    #     while left < right:
    #         if s[left] != s[right]:
    #             return self.isPalindrome(s, left + 1, right) or self.isPalindrome(s, left, right - 1)
    #         left += 1
    #         right -= 1
        
    #     return True


    # def isPalindrome(self, s, left, right):
    #     while left < right:
    #         if s[left] != s[right]:
    #             return False
    #         left += 1
    #         right -= 1

    #     return True 