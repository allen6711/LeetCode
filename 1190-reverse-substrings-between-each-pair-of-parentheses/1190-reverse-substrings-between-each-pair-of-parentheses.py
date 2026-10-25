class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for char in s:
            temp = []
            if char == ")":
                while stack and stack[-1] != "(":
                    temp.append(stack.pop())
                stack.pop()  # pop "("
                stack.extend(temp)
            else:
                stack.append(char)
        
        return "".join(stack)















        # Parentheses Matching + Direction Switching
        # O(n)
        # O(n)
        n = len(s)
        pair = [0] * n
        stack = []

        # Step 1: Match parentheses
        for i, char in enumerate(s):
            if char == "(":
                stack.append(i)
            elif char == ")":
                j = stack.pop()
                pair[i] = j
                pair[j] = i
            
        # Step 2: Traverse with direction switching
        ans = []
        i = 0
        direction = 1

        while 0 <= i < n:
            if s[i] == "(" or s[i] == ")":
                i = pair[i]
                direction *= -1
            else:
                ans.append(s[i])
            
            i += direction
        
        return "".join(ans)
        # O(n^2)
        # O(n)
        stack = []
        
        for char in s:
            if char == ")":
                temp = []

                while stack[-1] != "(":
                    temp.append(stack.pop())

                stack.pop()   # Remove "("
                stack.extend(temp)
            
            else:
                stack.append(char)
        
        return "".join(stack)