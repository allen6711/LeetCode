class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for word in strs:
            freq = [0] * 26
            for ch in word:
                freq[ord(ch) - ord('a')] += 1
            key = tuple(freq)
            groups[key].append(word)
        
        return list(groups.values())









        # O(klogk)
        # O(n*klogk)
        # groups = defaultdict(list)
        # for s in strs:
        #     key = "".join(sorted(s))
        #     groups[key].append(s)
        
        # return list(groups.values())
        # O(nk)
        # O(nk)
        groups = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for ch in s:
                count[ord(ch) - ord('a')] += 1
            key = tuple(count)
            groups[key].append(s)
        
        return list(groups.values())