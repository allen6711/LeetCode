class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = defaultdict(int)
        s2_count = defaultdict(int)
        left = 0
        n = len(s2)

        for char in s1:
            s1_count[char] += 1

        for right in range(n):
            s2_count[s2[right]] += 1
            if s2_count == s1_count:
                return True
            if (right - left + 1) >= len(s1):
                s2_count[s2[left]] -= 1
                if s2_count[s2[left]] == 0:
                    del s2_count[s2[left]]
                left += 1
        
        return False