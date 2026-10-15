class Solution:
    def firstUniqChar(self, s: str) -> int:
        # O(n)
        # O(n)
        # count = Counter(s)
        # for i, char in enumerate(s):
        #     if count[char] == 1:
        #         return i
            
        # return -1
        # O(n)
        # O(1)
        freq = [0] * 26
        for char in s:
            freq[ord(char) - ord('a')] += 1
        
        for i, char in enumerate(s):
            if freq[ord(char) - ord('a')] == 1:
                return i
            
        return -1