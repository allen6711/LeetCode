class Solution:
    def minWindow(self, s: str, t: str) -> str:
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