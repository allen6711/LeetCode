class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
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














        if len(s) != len(t):
            return False
        
        cnt = [0] * 26
        base = ord('a')

        for char in s:
            cnt[ord(char) - base] += 1
        
        for char in t:
            cnt[ord(char) - base] -= 1
            if cnt[ord(char) - base] < 0:
                return False
        
        return True

        # cnt = [0] * 26
        # base = ord('a')

        # for char in s:
        #     cnt[ord(char) - base] += 1
        
        # for char in t:
        #     cnt[ord(char) - base] -= 1
        
        # return all(x == 0 for x in cnt)


        # cnt = [0] * 26
        # base = ord('a')

        # for char in s:
        #     cnt[ord(char) - base] += 1
        
        # for char in t:
        #     cnt[ord(char) - base] -= 1
        
        # return all(x == 0 for x in cnt)

        # if len(s) != len(t):
        #     return False
            
        # cnt = [0] * 26
        # base = ord('a')

        # for char in s:
        #     cnt[ord(char) - base] += 1
        
        # for char in t:
        #     cnt[ord(char) - base] -= 1
        
        # return all(x == 0 for x in cnt)



        # if len(s) != len(t):
        #     return False
            
        # cnt = [0] * 26
        # base = ord('a')

        # for ch in s:
        #     cnt[ord(ch) - base] += 1
        
        # for ch in t:
        #     cnt[ord(ch) - base] -= 1
        
        # return all(x == 0 for x in cnt)

        # if len(s) != len(t):
        #     return False

        # cnt = [0] * 26
        # base = ord("a")

        # for ch in s:
        #     cnt[ord(ch) - base] += 1
        
        # for ch in t:
        #     index = ord(ch) - base
        #     cnt[index] -= 1
            
        #     if cnt[index] < 0:
        #         return False

        # return True