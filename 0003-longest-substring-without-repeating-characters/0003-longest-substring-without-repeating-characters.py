class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cur_set = set()
        left = 0
        max_len = 0

        for right in range(len(s)):
            while s[right] in cur_set:
                cur_set.remove(s[left])
                left += 1
            cur_set.add(s[right])
            max_len = max(max_len, right - left + 1)
        
        return max_len
            













        # O(n^3)
        # O(n)
        # n = len(s)
        # best = 0
        # for i in range(n):
        #     for j in range(i, n):
        #         sub = s[i:j + 1]
        #         if len(sub) == len(set(sub)):
        #             best = max(best, len(sub))
        
        # return best
        # O(n)
        # k = length of set
        # O(min(n, k))
        visited = set()
        n = len(s)
        left = 0
        best = 0
        for right in range(n):
            while s[right] in visited:
                visited.remove(s[left])
                left += 1

            visited.add(s[right])
            best = max(best, right - left + 1)
        
        return best