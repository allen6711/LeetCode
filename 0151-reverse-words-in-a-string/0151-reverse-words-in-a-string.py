class Solution:
    def reverseWords(self, s: str) -> str:
        # O(n)
        # O(n)
        # words = s.split()
        # words.reverse()
        # return " ".join(words)
        # O(n)
        # O(n)
        return " ".join(s.split()[::-1])
