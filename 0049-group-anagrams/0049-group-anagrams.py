class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for char in s:
                count[ord(char) - ord('a')] += 1

            key = tuple(count)
            ans[key].append(s)

        return list(ans.values())













        # O(klogk)
        # O(n*klogk)
        # groups = defaultdict(list)
        # for s in strs:
        #     key = "".join(sorted(s))
        #     groups[key].append(s)
        
        # return list(groups.values())
        # O(klogk)
        # O(nklogk)
        # groups = defaultdict(list)
        # for str in strs:
        #     key = tuple(sorted(str))
        #     groups[key].append(str)
        
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