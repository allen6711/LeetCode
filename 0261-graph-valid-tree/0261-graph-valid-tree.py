class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        
        # Create node dict
        neighbors = defaultdict(list)

        for u, v in edges:
            neighbors[u].append(v)
            neighbors[v].append(u)
        
        visited = {}
        queue = deque([0])
        visited[0] = True

        while queue:
            node = queue.popleft()

            for neighbor in neighbors[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited[neighbor] = True
        
        return len(visited) == n