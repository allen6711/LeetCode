class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return -1
        
        q = deque([(0, 0, 1)])
        visited = set([0, 0])
        while q:
            x, y, dist = q.popleft()
            if x == n - 1 and y == n - 1:
                return dist
            for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)):
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 0:
                    if (nx, ny) not in visited:
                        visited.add((nx, ny))
                        q.append((nx, ny, dist + 1))
        
        return -1












        # O(n^2)
        # O(n^2)
        # If start of end is blocked, no path exists
        n = len(grid)
        if grid[0][0] == 1 or grid[n - 1][n - 1]:
            return -1
        
        # Single cell grid and it is open
        if n == 1:
            return 1

        q = deque([(0, 0, 1)])  # row, col, path_length
        visited = set([0, 0])
        
        while q:
            x, y, dist = q.popleft()
            # If we reach the target, this is the shortest path length
            if x == n - 1 and y == n - 1:
                return dist
            for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1), 
                           (1, 1), (-1, -1), (1, -1), (-1, 1)):
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 0:
                    if (nx, ny) not in visited:
                        visited.add((nx, ny))
                        q.append((nx, ny, dist + 1))
        
        return -1




        count = 0
        
        q = deque([(0, 0)])

        while q:
            x, y = q.popleft()
            for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)):
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0:
                    grid[nx][ny] = 1
                    q.append((nx, ny))
                    count += 1
        
        return count if (x, y) == (rows - 1, cols - 1) else 0