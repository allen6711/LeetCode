class Solution:
    def reverseWords(self, s: str) -> str:
        # Two Pointer
        # O(n)
        # O(n)
        ans = []
        right = len(s) - 1

        while right >= 0:
            # Skip trailing spaces
            while right >= 0 and s[right] == " ":
                right -= 1
            
            if right < 0:
                break
            
            # Find the beginning of the word
            left = right
            while left >= 0 and s[left] != " ":
                left -= 1
            
            # Extract the word
            ans.append(s[left + 1:right + 1])

            # Move to the previous word
            right = left
        
        return " ".join(ans)
        # O(n)
        # O(n)
        words = s.split()
        words.reverse()
        return " ".join(words)
        # O(n)
        # O(n)
        return " ".join(s.split()[::-1])
