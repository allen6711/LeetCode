class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # BFS
        n = numCourses
        node_indegree = {x: 0 for x in range(n)}
        node_neighbors = {x: [] for x in range(n)}

        for to_node, from_node in prerequisites:
            node_indegree[to_node] += 1
            node_neighbors[from_node].append(to_node)

        start_nodes = [node for node in range(n) if node_indegree[node] == 0]
        queue = deque(start_nodes)
        order = []

        while queue:
            node = queue.popleft()
            order.append(node)
            
            for neighbor in node_neighbors[node]:
                node_indegree[neighbor] -= 1
                if node_indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        return order if len(order) == numCourses else []




        # graph = defaultdict(list)
        # indegrees = [0] * numCourses
        # course_order = []
        # for course, prerequsite in prerequisites:
        #     graph[prerequsite].append(course)
        #     indegrees[course] += 1
        
        # queue = deque([course_ini for course_ini in range(numCourses) if indegrees[course_ini] == 0])

        # while queue:
        #     course_ready = queue.popleft()
        #     course_order.append(course_ready)

        #     for successor in graph[course_ready]:
        #         indegrees[successor] -= 1

        #         if indegrees[successor] == 0:
        #             queue.append(successor)
        
        # return course_order if len(course_order) == numCourses else []