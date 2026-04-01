class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - ord('a')] += 1
        for ch in t:
            freq[ord(ch) - ord('a')] -= 1
        
        for count in freq:
            if count != 0:
                return False
        
        return True














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