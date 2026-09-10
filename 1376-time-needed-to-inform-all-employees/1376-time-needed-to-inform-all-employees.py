class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = [[] for _ in range(n)]

        for employee in range(n):
            if manager[employee] != -1:
                graph[manager[employee]].append(employee)
        
        def dfs(manager):
            if not graph[manager]:
                return 0
            
            max_time = 0

            for subordinate in graph[manager]:
                max_time = max(max_time, dfs(subordinate))
            
            return informTime[manager] + max_time
        
        return dfs(headID)