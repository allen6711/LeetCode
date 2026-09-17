class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # O(n^3)
        # O(1)
        # n = len(s)
        # best = 0
        # for i in range(n):
        #     for j in range(i, n):
        #         sub = s[i:j + 1]
        #         freq = Counter(sub)
        #         max_freq = max(freq.values())
                
        #         if (j - i + 1) - max_freq <= k:
        #             best = max(best, j - i + 1)
        # return best
        # O(n)
        # O(1)
        n = len(s)
        counts = defaultdict(int)
        max_count = 0
        left = 0
        ans = 0
        for right in range(n):
            counts[s[right]] += 1
            max_count = max(max_count, counts[s[right]])
            while (right - left + 1) - max_count > k:
                counts[s[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)
        
        return ans