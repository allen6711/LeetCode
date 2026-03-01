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
        # def dfs(sub: str) -> int:
        #     # If substring is shorter than k, impossible for any char to appear k times
        #     if len(sub) < k:
        #         return 0
        #     freq = Counter(sub)
        #     # Find a split character that appears fewer than k times
        #     for char, count in freq.items():
        #         if count < k:
        #             # Split by this invalid character and solve each segment
        #             best = 0
        #             for part in sub.split(char):
        #                 best = max(best, dfs(part))
        #             return best
            
        #     # If no invalid character exists, the whole substring is valid
        #     return len(sub)
        # return dfs(s)
        # O(n)
        # O(1)
        n = len(s)
        best = 0
        for target_unique in range(1, 27):
            count = [0] * 26
            left = 0
            right = 0
            unique_count = 0
            count_at_least_k = 0

            while right < n:
                idx = ord(s[right]) - ord('a')
                if count[idx] == 0:
                    unique_count += 1
                count[idx] += 1
                if count[idx] == k:
                    count_at_least_k += 1
                
                right += 1

                while unique_count > target_unique:
                    left_idx = ord(s[left]) - ord('a')
                    if count[left_idx] == k:
                        count_at_least_k -= 1
                    count[left_idx] -= 1
                    if count[left_idx] == 0:
                        unique_count -= 1
                    left += 1
                
                if unique_count == target_unique and count_at_least_k == target_unique:
                    best = max(best, right - left)
        return best