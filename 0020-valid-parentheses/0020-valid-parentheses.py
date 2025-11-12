class Solution:
    def isValid(self, s: str) -> bool:
        expected_dict = {")": "(", "]": "[", "}": "{"}
        stack = []

        for char in s:
            if char in "([{":
                stack.append(char)
            
            else:
                if not stack or stack[-1] != expected_dict[char]:
                    return False
                stack.pop()
        
        return not stack

        # expected_dict = {")": "(", "]": "[", "}": "{"}
        # stack = []

        # for ch in s:
        #     if ch in "([{":
        #         stack.append(ch)
            
        #     else:
        #         if not stack or stack[-1] != expected_dict.get(ch, None):
        #             return False
        #         stack.pop()
        
        # return not stack


        # expected_dict = {")": "(", "]": "[", "}": "{"}
        # stack = []

        # for char in s:
        #     if char in "([{":
        #         stack.append(char)
            
        #     else:
        #         if not stack or stack[-1] != expected_dict.get(char, None):
        #             return False
        #         stack.pop()
            
        # return not stack


        # stack = []
        # valid_pairs = {"()", "[]", "{}"}
        
        # for char in s:
        #     if char in "([{":
        #         stack.append(char)
            
        #     elif not stack or stack.pop() + char not in valid_pairs:
        #         return False
        
        # return not stack