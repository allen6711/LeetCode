class Solution:
    def isValid(self, s: str) -> bool:
        # O(n)
        # O(n)
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