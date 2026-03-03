class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        best = 0
        count = {}
        max_freq = 0
        left = 0
        for right in range(n):
            if s[right] in count:
                count[s[right]] += 1
            else:
                count[s[right]] = 1
            if count[s[right]] > max_freq:
                max_freq = count[s[right]]
            while (right - left + 1) - max_freq > k:
                left_char = s[left]
                count[left_char] -= 1
                left += 1
            best = max(best, right - left + 1)
        return best
















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
        count = {}
        max_freq = 0
        best = 0
        left = 0
        for right in range(n):
            char = s[right]
            # Expanding counting logic
            if char in count:
                count[char] += 1
            else:
                count[char] = 1
            if count[char] > max_freq:
                max_freq = count[char]
            while (right - left + 1 - max_freq) > k:
                left_char = s[left]
                count[left_char] -= 1
                left += 1
            best = max(best, right - left + 1)
        return best  