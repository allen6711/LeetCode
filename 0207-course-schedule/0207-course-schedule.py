class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = [0] * numCourses
        for pre, course in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1
        
        q = deque()
        completed = 0
        
        for course in range(numCourses):
            if indegree[course] == 0:
                q.append(course)
            
        while q:
            cur = q.popleft()
            completed += 1

            for next_course in graph[cur]:
                indegree[next_course] -= 1

                if indegree[next_course] == 0:
                    q.append(next_course)
        
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