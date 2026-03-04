class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        dist = [[-1] * cols for _ in range(rows)]
        q = deque()

        # Multi-source initialization: all 0s are sources
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    dist[r][c] = 0
                    q.append((r, c))
        
        # BFS
        while q:
            x, y = q.popleft()
            for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))
        
        return dist
