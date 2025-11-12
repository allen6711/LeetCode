class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n
        index_stack = []

        for i, temp in enumerate(temperatures):
            while index_stack and temperatures[index_stack[-1]] < temp:
                j = index_stack.pop()
                answer[j] = i - j

            index_stack.append(i)
        
        return answer












        # answer = [0] * len(temperatures)
        # stack = []

        # for index, current_temp in enumerate(temperatures):
        #     while stack and temperatures[stack[-1]] < current_temp:
        #         previous_index = stack.pop()
        #         answer[previous_index] = index - previous_index
            
        #     stack.append(index)
        
        # return answer