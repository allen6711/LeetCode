class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # O(V+E), V: numCourses, E: len(prerequisities)
        # O(V+E)
        # Build graph: pre -> list of courses that depend on it
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1
        
        # Start with all courses that have no prerequisites
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        taken = 0

        while q:
            cur = q.popleft()
            taken += 1
            for next in graph[cur]:
                indegree[next] -= 1
                if indegree[next] == 0:
                    q.append(next)
        
        return taken == numCourses

        














        # BFS
        n = numCourses
        node_indegree = {x: 0 for x in range(n)}
        node_neighbors = {x: [] for x in range(n)}

        for to_node, from_node in prerequisites:
            node_indegree[to_node] += 1
            node_neighbors[from_node].append(to_node)
        
        start_nodes = [node for node in range(n) if node_indegree[node] == 0]
        queue = deque(start_nodes)
        result = []

        while queue:
            node = queue.popleft()
            result.append(node)
            for neighbor in node_neighbors[node]:
                node_indegree[neighbor] -= 1
                if node_indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        return len(result) == numCourses

        # graph = defaultdict(list)
        # indegrees = [0] * numCourses
        # completed_count = 0
        # for course, prereq in prerequisites:
        #     graph[prereq].append(course)
        #     indegrees[course] += 1
        
        # queue = deque([i for i in range(numCourses) if indegrees[i] == 0])

        # while queue:
        #     course_ready = queue.popleft()
        #     completed_count += 1

        #     for successor in graph[course_ready]:
        #         indegrees[successor] -= 1

        #         if indegrees[successor] == 0:
        #             queue.append(successor)

        # return completed_count == numCourses
