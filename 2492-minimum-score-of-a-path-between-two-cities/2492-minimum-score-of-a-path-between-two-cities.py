class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)

        for a, b, dist in roads:
            graph[a].append((b, dist))
            graph[b].append((a, dist))
        
        visited = set()
        queue = deque([1])
        visited.add(1)
        answer = float('inf')

        while queue:
            city = queue.popleft()

            for neighbor, distance in graph[city]:
                answer = min(answer, distance)

                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        
        return answer   