class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        for (a, b), value in zip(equations, values):
            graph[a].append((b, value))
            graph[b].append((a, 1 / value))
        
        def bfs(start: str, target: str) -> float:
            if start not in graph or target not in graph:
                return -1.0
            
            if start == target:
                return 1.0
            
            q = deque([(start, 1.0)])
            visited = set([start])
            while q:
                cur, cur_value = q.popleft()
                for nei, weight in graph[cur]:
                    if nei in visited:
                        continue

                    next_value = cur_value * weight
                    if nei == target:
                        return next_value
                    
                    visited.add(nei)
                    q.append((nei, next_value))
            
            return -1.0
        
        ans = []
        for a, b in queries:
            ans.append(bfs(a, b))
        
        return ans

        # N = number of equations
        # Q = number of queries
        # V = number of variables
        # E = number of graph edges
        # O(N+Q*(V+E))
        # O(V+E)
        graph = defaultdict(list)
        # Build graph
        for (a, b), value in zip(equations, values):
            graph[a].append((b, value))
            graph[b].append((a, 1 / value))
        
        def bfs(start: str, target: str) -> float:
            # If either variable does not exist, answer is -1.0
            if start not in graph or target not in graph:
                return  -1.0
            
            # x / x = 1.0 if x exists in graph
            if start == target:
                return 1.0
            
            q = deque([(start, 1.0)])
            visited = set([start])

            while q:
                cur, cur_value = q.popleft()

                for nei, weight in graph[cur]:
                    if nei in visited:
                        continue
                    
                    next_value = cur_value * weight

                    if nei == target:
                        return next_value
                    
                    visited.add(nei)
                    q.append((nei, next_value))
            
            return -1.0
        
        ans = []

        for a, b in queries:
            ans.append(bfs(a, b))
        
        return ans