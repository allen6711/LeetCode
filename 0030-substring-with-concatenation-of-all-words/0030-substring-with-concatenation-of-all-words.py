class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        
        wLen = len(words[0])
        k = len(words)
        totalLen = wLen * k
        n = len(s)

        if n < totalLen:
            return []
        
        need = Counter(words)
        ans = []

        for offset in range(wLen):
            left = offset
            window = defaultdict(int)
            matched = 0

            for right in range(offset, n - wLen + 1, wLen):
                word = s[right: right + wLen]

                if word not in need:
                    window.clear()
                    matched = 0
                    left = right + wLen
                    continue
                
                window[word] += 1
                matched += 1

                while window[word] > need[word]:
                    left_word = s[left: left + wLen]
                    window[left_word] -= 1
                    matched -= 1
                    left += wLen
                
                if matched == k:
                    ans.append(left)
                    left_word = s[left: left + wLen]
                    window[left_word] -= 1
                    matched -= 1
                    left += wLen
            
        return ans




        # if not s or not words:
        #     return []
        
        # wLen = len(words[0])
        # k = len(words)
        # totalLen = wLen * k
        # n = len(s)

        # if n < totalLen:
        #     return []

        # need = Counter(words)
        # ans = []

        # for offset in range(wLen):
        #     left = offset
        #     window = defaultdict(int)
        #     matched = 0

        #     for right in range(offset, n - wLen + 1, wLen):
        #         w = s[right: right + wLen]

        #         if w not in need:
        #             window.clear()
        #             matched = 0
        #             left = right + wLen
        #             continue
                
        #         window[w] += 1
        #         matched += 1

        #         # shrink if w is over-counted
        #         while window[w] > need[w]:
        #             left_word = s[left: left + wLen]
        #             window[left_word] -= 1
        #             matched -= 1
        #             left += wLen
                
        #         # if window has exactly k words, record answer
        #         if matched == k:
        #             ans.append(left)
        #             left_word = s[left: left + wLen]
        #             window[left_word] -= 1
        #             matched -= 1
        #             left += wLen
        
        # return ans