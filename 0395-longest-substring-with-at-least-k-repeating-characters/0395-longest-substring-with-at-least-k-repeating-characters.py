class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        # O(n^3)
        # O(1)
        # n = len(s)
        # best = 0
        # for i in range(n):
        #     for j in range(i, n):
        #         sub = s[i:j + 1]
        #         freq = Counter(sub)
                
        #         valid = True
        #         for count in freq.values():
        #             if count < k:
        #                 valid = False
        #                 break
        #         if valid:
        #             best = max(best, j - i + 1)
        # return best
        # O(n^2)
        # O(n)
        def dfs(sub: str) -> int:
            # If substring is shorter than k, impossible for any char to appear k times
            if len(sub) < k:
                return 0
            freq = Counter(sub)
            # Find a split character that appears fewer than k times
            for char, count in freq.items():
                if count < k:
                    # Split by this invalid character and solve each segment
                    best = 0
                    for part in sub.split(char):
                        best = max(best, dfs(part))
                    return best
            
            # If no invalid character exists, the whole substring is valid
            return len(sub)
        return dfs(s)