class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # O(m*n)
        # O(m*n)
        # DFS
        rows, cols = len(grid), len(grid[0])
        islands = 0
        def dfs(r: int, c: int):
            if not (0 <= r < rows and 0 <= c < cols) or grid[r][c] == '0':
                return
            
            grid[r][c] = '0'

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    islands += 1
                    dfs(i, j)
        
        return islands
        # O(m*n)
        # O(m*n)
        # BFS
        if not grid and not grid[0]:
            return 0
        
        islands = 0
        rows, cols = len(grid), len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != '1':
                    continue
                
                islands += 1
                # mark visited
                grid[r][c] = '0'
                q = deque([(r, c)])
                
                while q:
                    x, y = q.popleft()
                    for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == '1':
                            grid[nx][ny] = '0'
                            q.append((nx, ny))
        
        return islands