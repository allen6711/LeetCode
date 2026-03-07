class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        islands = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != '1':
                    continue
                
                islands += 1
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













        # O(mn)
        # O(mn)
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
        # DFS
        # def dfs(row, col):
        #     grid[row][col] = '0'
        #     for dx, dy in zip(directions[:-1], directions[1:]):
        #         new_row, new_col = row + dx, col + dy
        #         if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] == '1':
        #             dfs(new_row, new_col)

        # island_count = 0
        # directions = [-1, 0, 1, 0, -1]
        # rows, cols = len(grid), len(grid[0])
        # for row in range(rows):
        #     for col in range(cols):
        #         if grid[row][col] == '1':
        #             dfs(row, col)
        #             island_count += 1
        
        # return island_count