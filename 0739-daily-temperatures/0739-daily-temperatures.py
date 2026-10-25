class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        stack = []
        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_i = stack.pop()
                ans[prev_i] = i - prev_i

            stack.append(i)
        
        return ans












        # O(n)
        # O(n)
        n = len(temperatures)
        result = [0] * n
        stack = []

        for i in range(n):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                prev = stack.pop()
                result[prev] = i - prev

            stack.append(i)
        
        return result