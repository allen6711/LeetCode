class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = Counter(magazine)
        for ch in ransomNote:
            if count[ch] == 0:
                return False
            else:
                count[ch] -= 1
        
        return True














        # O(n*m)
        # O(m)
        # magazine = list(magazine)
        # for ch in ransomNote:
        #     if ch in magazine:
        #         magazine.remove(ch)
        #     else:
        #         return False
        
        # return True
        # Hashmap
        # O(m+n)
        # O(m)
        # count = {}
        # for ch in magazine:
        #     count[ch] = count.get(ch, 0) + 1
        # for ch in ransomNote:
        #     if count.get(ch, 0) == 0:
        #         return False
        #     else:
        #         count[ch] -= 1
        
        # return True
        # Counter
        # O(m+n)
        # O(m)
        count = Counter(magazine)
        for ch in ransomNote:
            if count[ch] == 0:
                return False
            else:
                count[ch] -= 1
        return True