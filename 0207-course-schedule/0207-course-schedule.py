class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        for course, pre in prerequisites:
            graph[pre].append(course)
        
        state = [0] * numCourses

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
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        
        
        return True
        # DFS, Cycle Detection
        # O(V+E)
        # O(V+E)
        graph = [[] for _ in range(numCourses)]

        for course, pre in prerequisites:
            graph[pre].append(course)
        
        state = [0] * numCourses

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
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True
        # BFS, Topological Sort (Kahn's Algorithm)
        # V: numCourses
        # e: len(prerequisites)
        # O(V+E)
        # O(V+E)
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1
        
        dq = deque([])
        for i in range(numCourses):
            if indegree[i] == 0:
                dq.append(i)
        
        completed = 0
        while dq:
            cur = dq.popleft()
            completed += 1
            
            for neighbor in graph[cur]:
                indegree[neighbor] -= 1

                if indegree[neighbor] == 0:
                    dq.append(neighbor)
        
        return completed == numCourses















        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1
        
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        completed = 0

        while q:
            course = q.popleft()
            completed += 1
            
            for neighbor in graph[course]:
                indegree[neighbor] -= 1

                if indegree[neighbor] == 0:
                    q.append(neighbor)

        return completed == numCourses














        # O(V+E), V: numCourses, E: len(prerequisities)
        # O(V+E)
        # Build graph: pre -> list of courses that depend on it
        graph = defaultdict(list)
        indegree = [0] * numCourses

        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1
        
        # Start with all courses that have no prerequisites
        q = deque()
        for course in range(numCourses):
            if indegree[course] == 0:
                q.append(course)

        taken = 0

        while q:
            cur = q.popleft()
            taken += 1
            for next_course in graph[cur]:
                indegree[next_course] -= 1
                if indegree[next_course] == 0:
                    q.append(next_course)
        
        return taken == numCourses