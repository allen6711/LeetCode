class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        visited = [False] * n
        answer = 0

        def dfs(node: int) -> tuple[int, int]:
            visited[node] = True
            vertex_sum = 1
            degree_sum = len(graph[node])
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    child_vertex_sum, child_degree_sum = dfs(neighbor)
                    vertex_sum += child_vertex_sum
                    degree_sum += child_degree_sum
            
            return vertex_sum, degree_sum
        
        for node in range(n):
            if not visited[node]:
                vertex_sum, degree_sum = dfs(node)
                expected_degree_sum = vertex_sum * (vertex_sum - 1) // 2
                real_degree_sum = degree_sum // 2

                if real_degree_sum == expected_degree_sum:
                    answer += 1
        
        return answer















        graph = [[] for _ in range(n)]

        # Build the undirected graph
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        visited = [False] * n
        answer = 0

        def dfs(node: int) -> tuple[int, int]:
            visited[node] = True

            # Number of vertices in this connected component
            vertex_count = 1

            # Sum of degrees in this connected component
            degree_sum = len(graph[node])

            for neighbor in graph[node]:
                if not visited[neighbor]:
                    child_vertices, child_degree_sum = dfs(neighbor)
                    vertex_count += child_vertices
                    degree_sum += child_degree_sum
            
            return vertex_count, degree_sum

        for node in range(n):
            if not visited[node]:
                vertex_count, degree_sum = dfs(node)

                # Each undirected edge is counted twice
                edge_count = degree_sum // 2

                # A complete graph with k vertices has k * (k - 1) / 2 edges
                expected_edges = vertex_count * (vertex_count - 1) // 2
                if edge_count == expected_edges:
                    answer += 1
        
        return answer