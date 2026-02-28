class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # O(n^2)
        # O(k)
        # if not s or not t:
        #     return ""
        # need = Counter(t)
        # best_len = float('inf')
        # best_sub = ""
        # n = len(s)
        # for i in range(n):
        #     window = Counter()
        #     for j in range(i, n):
        #         sub = s[i:j + 1]
        #         window[s[j]] += 1
        #         # Check if current window satisfies all requirements
        #         valid = True
        #         for char, cnt in need.items():
        #             if window[char] < cnt:
        #                 valid = False
        #                 break
        #         if valid:
        #             if j - i + 1 < best_len:
        #                 best_len = j - i + 1
        #                 best_sub = s[i:j + 1]
        #             break  # For fixed i, this is already the shortest valid window
        
        # return best_sub
        # O(n) (O(|s)+|t|)
        # O(k)
        if not s or not t:
            return ""
        need = Counter(t)
        window = defaultdict(int)
        have = 0
        need_char_num = len(need)
        best_len = float('inf')
        best_left = 0
        left = 0

        for right, char in enumerate(s):
            window[char] += 1

            # The character reached the required count
            if char in need and window[char] == need[char]:
                have += 1
            
            # Try to shrink while the window is valid
            while have == need_char_num:
                window_len = right - left + 1
                if window_len < best_len:
                    best_len = window_len
                    best_left = left
                
                # Pop from the left
                left_char = s[left]
                window[left_char] -= 1
                # Window becomes invalid after removing left_char
                if left_char in need and window[left_char] < need[left_char]:
                    have -= 1
                left += 1
        
        return "" if best_len == float('inf') else s[best_left:best_left + best_len]



















        if not s or not t:
            return ""
        
        need = Counter(t)
        window = defaultdict(int)

        required = len(need)
        formed = 0

        left = 0
        best_len = float('inf')
        best_l = 0

        for right, char in enumerate(s):
            window[char] += 1
            if char in need and window[char] == need[char]:
                formed += 1
            while formed == required:
                if right - left + 1 < best_len:
                    best_len = right - left + 1
                    best_l = left
                
                left_char = s[left]
                window[left_char] -= 1
                if left_char in need and window[left_char] < need[left_char]:
                    formed -= 1
                left += 1
        return "" if best_len == float('inf') else s[best_l: best_l + best_len]