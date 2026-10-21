class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # DFS, Cycle Detection
        # O(V+E)
        # O(V+E)
        graph = [[] for _ in range(numCourses)]
        for course, pre in prerequisites:
            graph[pre].append(course)

        state = [0] * numCourses
        ans = []
        def dfs(course):
            if state[course] == 1:
                return False
            if state[course] == 2:
                return True
            
            state[course] = 1
            for neighbor in graph[course]:
                if not dfs(neighbor):
                    return False
            state[course] = 2
            ans.append(course)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return ans[::-1]
        # BFS, Topological Sort
        # V: numCourses (Vertex)
        # E: prerequisites (Edge)
        # O(V+E)
        # O(V+E)
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1
        
        ans = []

        dq = deque([])
        for course in range(numCourses):
            if indegree[course] == 0:
                dq.append(course)
        
        completed = 0
        while dq:
            cur = dq.popleft()
            completed += 1
            ans.append(cur)
            for neighbor in graph[cur]:
                indegree[neighbor] -= 1

                if indegree[neighbor] == 0:
                    dq.append(neighbor)
        
        return ans if completed == numCourses else []