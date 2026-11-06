class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_dict = {}
        ans = []
        for s in strs:
            count = [0] * 26
            for char in s:
                count[ord(char) - ord('a')] += 1
            key = tuple(count)
            if key not in group_dict:
                group_dict[key] = [s]
            else:
                group_dict[key].append(s)
        
        return list(group_dict.values())












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
        # k: max string length
        groups = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for ch in s:
                count[ord(ch) - ord('a')] += 1
            key = tuple(count)
            groups[key].append(s)
        
        return list(groups.values())