class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = [0] * numCourses
        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1
        
        completed = 0
        q = deque()
        for course in range(numCourses):
            if indegree[course] == 0:
                q.append(course)
        
        ans = []
        while q:
            cur = q.popleft()
            completed += 1
            ans.append(cur)
            for next_course in graph[cur]:
                indegree[next_course] -= 1
                
                if indegree[next_course] == 0:
                    q.append(next_course)
        
        return ans if completed == numCourses else []















        # V = numCourses
        # E = len(prerequisites)
        # O(V+E)
        # O(V+E)
        graph = defaultdict(list)
        indegree = [0] * numCourses

        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1
        
        q = deque()
        ans = []
        completed = 0
        for course in range(numCourses):
            if indegree[course] == 0:
                q.append(course)
            
        while q:
            cur = q.popleft()
            ans.append(cur)
            completed += 1
            for next_course in graph[cur]:
                indegree[next_course] -= 1

                if indegree[next_course] == 0:
                    q.append(next_course)
        
        return ans if completed == numCourses else []