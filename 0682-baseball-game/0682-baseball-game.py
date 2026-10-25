class Solution:
    def calPoints(self, operations: list[str]) -> int:
        stack = []
        for char in operations:
            if char not in "CD+":
                stack.append(int(char))
            
            else:
                if char == "C":
                   stack.pop()
                elif char == "D":
                    stack.append(2 * stack[-1])
                else:
                    stack.append(stack[-1] + stack[-2])
        
        return sum(stack)