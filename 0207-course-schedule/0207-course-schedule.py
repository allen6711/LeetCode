class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
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