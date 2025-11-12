class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = defaultdict(list)
        base = ord('a')

        for char in strs:
            cnt = [0] * 26
            for ch in char:
                cnt[ord(ch) - base] += 1
            
            key = tuple(cnt)
            answer[key].append(char)
        
        return list(answer.values())















        # anagrams = defaultdict(list)
        # for s in strs:
        #     key = "".join(sorted(s))
        #     anagrams[key].append(s)
        
        # return list(anagrams.values())