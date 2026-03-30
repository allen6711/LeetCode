class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # O(n*m)
        # O(m)
        # magazine = list(magazine)
        # for ch in ransomNote:
        #     if ch in magazine:
        #         magazine.remove(ch)
        #     else:
        #         return False
        
        # return True
        # O()
        # O()
        count = {}
        for ch in magazine:
            count[ch] = count.get(ch, 0) + 1
        for ch in ransomNote:
            if count.get(ch, 0) == 0:
                return False
            else:
                count[ch] -= 1
        
        return True