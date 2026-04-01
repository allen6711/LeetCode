class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_to_t = {}
        t_to_s = {}
        for ch_s, ch_t in zip(s, t):
            if ch_s in s_to_t and s_to_t[ch_s] != ch_t:
                return False
            if ch_t in t_to_s and t_to_s[ch_t] != ch_s:
                return False
            s_to_t[ch_s] = ch_t
            t_to_s[ch_t] = ch_s
        
        return True
            













        # O(n^2)
        # O(1)
        # n = len(s)
        # for i in range(n):
        #     for j in range(i + 1, n):
        #         if (s[i] == s[j] and t[i] != t[j]) or (s[i] != s[j] and t[i] == t[j]):
        #             return False
        
        # return True
        # O(n)
        # O(n)
        s_to_t = {}
        t_to_s = {}
        for char_s, char_t in zip(s, t):
            if char_s in s_to_t and s_to_t[char_s] != char_t:
                return False
            if char_t in t_to_s and t_to_s[char_t] != char_s:
                return False
            
            s_to_t[char_s] = char_t
            t_to_s[char_t] = char_s

        return True
