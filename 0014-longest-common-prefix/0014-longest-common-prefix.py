class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # O(nL)
        # O(1)
        if not strs:
            return ""
        
        first = strs[0]

        for i in range(len(first)):
            expected = first[i]
            for j in range(1, len(strs)):
                # If current string is too short or char mismatches
                if i >= len(strs[j]) or strs[j][i] != expected:
                    return first[:i] # slicing costs O(i)
        
        return first









        for index in range(len(strs[0])):
            for string in strs[1:]:
                if index >= len(string) or strs[0][index] != string[index]:
                    return strs[0][:index]
        
        return strs[0]