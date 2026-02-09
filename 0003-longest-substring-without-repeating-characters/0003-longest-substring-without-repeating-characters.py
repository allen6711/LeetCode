class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last = {}  # char -> last index
        left = 0
        best = 0

        for right, char in enumerate(s):
            if char in last and last[char] >= left:
                left = last[char] + 1
            
            last[char] = right
            best = max(best, right - left + 1)
        
        return best

















        # unique_chars = set()
        # max_length = 0
        # left_pointer = 0
        # for right_pointer, char in enumerate(s):
        #     while char in unique_chars:
        #         unique_chars.remove(s[left_pointer])
        #         left_pointer += 1
                
        #     unique_chars.add(s[right_pointer])
        #     max_length = max(max_length, right_pointer - left_pointer + 1)
        
        # return max_length