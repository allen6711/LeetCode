class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        neighbors = defaultdict(list)

        for u, v in edges:
            neighbors[u].append(v)
            neighbors[v].append(u)
        
        visited = set()
        components = 0
        
        for start in range(n):
            if start in visited:
                continue

            queue = deque([start])
            visited.add(start)
            components += 1
            
            while queue:
                cur = queue.popleft()

                for neighbor in neighbors[cur]:
                    if neighbor not in visited:
                        queue.append(neighbor)
                        visited.add(neighbor)
            
        return components
