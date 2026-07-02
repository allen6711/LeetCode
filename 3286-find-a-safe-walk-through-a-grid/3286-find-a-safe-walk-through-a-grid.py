class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        # O(m*n)
        # O(m*n)
        m, n = len(grid), len(grid[0])
        dist = [[float('inf')] * n for _ in range(m)]
        dist[0][0] = grid[0][0]

        queue = deque([(0, 0)])
        
        while queue:
            r, c = queue.popleft()
            for dr, dc in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    new_cost = dist[r][c] + grid[nr][nc]

                    if new_cost < dist[nr][nc]:
                        dist[nr][nc] = new_cost

                        if grid[nr][nc] == 0:
                            queue.appendleft((nr, nc))
                        else:
                            queue.append((nr, nc))

        return dist[m - 1][n - 1] < health