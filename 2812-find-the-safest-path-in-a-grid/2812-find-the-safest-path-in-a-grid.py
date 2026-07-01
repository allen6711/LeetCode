class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)

        # Step 1: multi-source BFS to compute distance to nearest thief
        dist = [[-1] * n for _ in range(n)]
        queue = deque()

        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    dist[r][c] = 0
                    queue.append((r, c))
        
        while queue:
            r, c = queue.popleft()
            for dr, dc in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and dist[nr][nc] == -1:
                    dist[nr][nc] = dist[r][c] + 1
                    queue.append((nr, nc))
        # Step 2: max heap to find path with maximum minimum distance
        visited = [[False] * n for _ in range(n)]

        # heap stores (-safeness, r, c)
        # use negative because Python heapq is min heap
        heap = [(-dist[0][0], 0, 0)]
        visited[0][0] = True

        while heap:
            safeness, r, c = heapq.heappop(heap)
            safeness = -safeness

            if r == n - 1 and c == n - 1:
                return safeness
            
            for dr, dc in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                nr, nc = r + dr, c + dc

                if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                    visited[nr][nc] = True

                    new_safeness = min(safeness, dist[nr][nc])
                    heapq.heappush(heap, (-new_safeness, nr, nc))
        
        return 0