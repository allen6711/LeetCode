class Solution:
    def reverseWords(self, s: str) -> str:
        word = s.strip().split()
        n = len(word)
        ans = []
        for i in range(n - 1, -1, -1):
            ans.append(word[i])
        return " ".join(ans)
