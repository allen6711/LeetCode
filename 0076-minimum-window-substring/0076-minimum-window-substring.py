class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need_ch_num = Counter(t)
        window = defaultdict(int)
        need_ch = len(need_ch_num)
        now_have = 0

        left = 0
        best_left = 0
        best_len = float('inf')

        for right, char in enumerate(s):
            window[char] += 1
            if window[char] == need_ch_num[char]:
                now_have += 1

            while now_have == need_ch:
                cur_len = right - left + 1
                if cur_len < best_len:
                    best_len = cur_len
                    best_left = left
                
                window[s[left]] -= 1
                if s[left] in need_ch_num and window[s[left]] < need_ch_num[s[left]]:
                    now_have -= 1

                left += 1
        
        if best_len == float('inf'):
            return ""
        
        return s[best_left:best_left + best_len]









        # O(n^3)
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
        need = Counter(t)
        window = defaultdict(int)

        required = len(need)
        formed = 0

        left = 0
        min_len = float('inf')
        min_left = 0

        for right, char in enumerate(s):
            window[char] += 1

            # The character reached the required count
            if char in need and window[char] == need[char]:
                formed += 1
            
            # Try to shrink while the window is valid
            while formed == required:
                if right - left + 1 < min_len:
                    min_len  = right - left + 1
                    min_left = left
                
                # Pop from the left
                left_char = s[left]
                window[left_char] -= 1
                # Window becomes invalid after removing left_char
                if left_char in need and window[left_char] < need[left_char]:
                    formed -= 1
                left += 1
        
        return "" if min_len == float('inf') else s[min_left:min_left + min_len]