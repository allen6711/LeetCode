class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # O(n)
        # O(n)
        # word = s.strip().split()
        # return len(word[-1])
        # O(n)
        # O()
        right = len(s) - 1
        # Skip trailing spaces
        while right >= 0 and s[right] == " ":
            right -= 1
        length = 0
        # Count the last word
        while right >= 0 and s[right] != " ":
            length += 1
            right -= 1
        
        return length