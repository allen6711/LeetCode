class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # O(n*m)
        # O(1)
        if not strs:
            return ""
        
        first = strs[0]
        for i in range(len(first)):
            ch = first[i]
            for s in strs[1:]:
                if i >= len(s) or s[i] != ch:
                    return first[:i]
        return first