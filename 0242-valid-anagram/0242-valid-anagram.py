class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count_s = [0] * 26
        count_t = [0] * 26
        for char_s in s:
            count_s[ord(char_s) - ord('a')] += 1 
        for char_t in t:
            count_t[ord(char_t) - ord('a')] += 1
        
        return count_s == count_t



        if len(s) != len(t):
            return False
        
        s_counter = Counter(s)
        return Counter(t) == s_counter
        














        # O(nlogn)
        # O(n)
        # return sorted(s) == sorted(t)
        # O(n)
        # O(k)
        # return Counter(s) == Counter(t)
        # O(n)
        # O(1)
        if len(s) != len(t):
            return False
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - ord('a')] += 1
        for ch in t:
            freq[ord(ch) - ord('a')] -= 1
        for count in freq:
            if count != 0:
                return False
        return True