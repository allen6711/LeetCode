class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # O(nm)
        # O(1)
        # n = len(haystack)
        # m = len(needle)

        # for i in range(n - m + 1):
        #     for j in range(m):
        #         if haystack[i + j] != needle[j]:
        #             break
        #     else:
        #         return i
        # return -1
        # O(n + m)
        # O(m)
        if needle == "":
            return 0
        n = len(haystack)
        m = len(needle)

        lps = [0] * m
        length = 0
        i = 1

        while i < m:
            if needle[i] == needle[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        i = 0  # pointer for haystack
        j = 0  # pointer for needle
        while i < n:
            if haystack[i] == needle[j]:
                i += 1
                j += 1

                if j == m:
                    return i - m
            else:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1
        return -1
