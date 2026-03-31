class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s = Counter(s)
        count_t = Counter(t)
        if count_s == count_t:
            return True
        else:
            return False














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