class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # O(n)
        # O(min(n, k))
        # k: length of set
        left = 0
        n = len(s)
        max_length = 0
        visited = set()
        for right in range(n):
            while s[right] in visited:
                visited.remove(s[left])
                left += 1
            visited.add(s[right])
            max_length = max(max_length, right - left + 1)
        
        return max_length