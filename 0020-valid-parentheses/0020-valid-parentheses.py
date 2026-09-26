class Solution:
    def isValid(self, s: str) -> bool:
        # O(n)
        # O()
        # 因為括號要遵守：最後打開的括號，要最先被關閉。
        # 也就是：Last In, First Out (LIFO)
        pair = {")": "(", "]": "[", "}": "{"}
        stack = []

        for char in s:
            if char in "([{":
                stack.append(char)
            
            else:
                if not stack or stack[-1] != pair[char]:
                    return False
                
                stack.pop()
        
        return len(stack) == 0















        
        expected_dict = {")": "(", "]": "[", "}": "{"}
        stack = []

        for char in s:
            if char in "([{":
                stack.append(char)
            
            else:
                if not stack or stack[-1] != expected_dict.get(char, None):
                    return False
                stack.pop()
        
        return not stack


        # expected_dict = {")": "(", "]": "[", "}": "{"}
        # stack = []

        # for char in s:
        #     if char in "([{":
        #         stack.append(char)
            
        #     else:
        #         if not stack or stack[-1] != expected_dict[char]:
        #             return False
        #         stack.pop()
        
        # return not stack

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