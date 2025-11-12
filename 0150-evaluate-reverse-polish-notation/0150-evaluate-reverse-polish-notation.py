class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        num_stack = []

        for token in tokens:
            if token not in {"+", "-", "*", "/"}:
                num_stack.append(int(token))
            
            else:
                b = num_stack.pop()
                a = num_stack.pop()
                if token == "+":
                    num_stack.append(a + b)
                
                if token == "-":
                    num_stack.append(a - b)
                
                if token == "*":
                    num_stack.append(a * b)
                
                if token == "/":
                    num_stack.append(int(a / b))
                
        return num_stack[-1]

        # stack = []
        # for token in tokens:
        #     if token not in {"+", "-", "*", "/"}:
        #         stack.append(int(token))
            
        #     else:
        #         b = stack.pop()
        #         a = stack.pop()
        #         if token == "+":
        #             stack.append(a + b)
        #         if token == "-":
        #             stack.append(a - b)
        #         if token == "*":
        #             stack.append(a * b)
        #         if token == "/":
        #             stack.append(int(a / b))
        
        # return stack[-1]