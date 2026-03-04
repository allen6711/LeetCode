class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        fresh = 0
        minutes = 0
        q = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r, c))
        
        while q and fresh > 0:
            level_size = len(q)
            for _ in range(level_size):
                x, y = q.popleft()
                for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        fresh -= 1
                        q.append((nx, ny))
            minutes += 1
        
        return minutes if fresh == 0 else -1



















        rows, cols = len(grid), len(grid[0])
        minutes = 0
        fresh = 0
        q = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r, c))
        
        if fresh == 0:
            return 0
        
        while q and fresh > 0:
            level_size = len(q)
            for _ in range(level_size):
                x, y = q.popleft()
                for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        fresh -= 1
                        q.append((nx, ny))
            minutes += 1
        
        return minutes if fresh == 0 else -1


















        # O(mn)
        # O(mn)
        if not grid or not grid[0]:
            return -1

        rows, cols = len(grid), len(grid[0])
        q = deque()
        fresh = 0

        # 1) Initialize queue with all rotten oranges (multi-source)
        #    and count fresh oranges
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1
        # No fresh
        if fresh == 0:
            return 0
        
        minutes = 0
        # 2) BFS by levels (each level = 1 minute)
        while q and fresh > 0:
            level_size = len(q)
            for _ in range(level_size):
                x, y = q.popleft()
                for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        fresh -= 1
                        q.append((nx, ny))
            minutes += 1
        
        return minutes if fresh == 0 else -1