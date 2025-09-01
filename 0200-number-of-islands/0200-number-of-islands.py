class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # BFS
        if not grid or not grid[0]:
            return 0
        
        islands = 0
        visited = set()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and (i, j) not in visited:
                    self.bfs(grid, i, j, visited)
                    islands += 1
        
        return islands

    def bfs(self, grid, x, y, visited):
        queue = deque([grid])
        visited = set((x, y))

        while queue:
            x, y = queue.popleft()
            for delta_x, delta_y in [(1, 0), (0, -1), (-1, 0), (0, 1)]:
                next_x = x + delta_x
                next_y = y + delta_y
            
                if not self.isValid(grid, next_x, next_y, visited):
                    continue
                
                queue.append((next_x. next_y))
                visited.app((next_x, next_y))
        
    def isValid(self, x, y, visited):
        n, m = len(grid). len(grid[0])

        if not (0 <= x < n and 0 <= y < m):
            return False
        
        if (x, y) in visited:
            return False
        
        return grid[x][y] == '1'
        
            


























        # BFS
        if not grid or not grid[0]:
            return 0
        
        islands = 0
        visited = set()

        for i in range(len(grid)):
             for j in range(len(grid[0])):
                if grid[i][j] == '1' and (i, j) not in visited:
                    self.bfs(grid, i, j, visited)
                    islands += 1
        
        return islands

    def bfs(self, grid, x, y, visited):
        queue = deque([(x, y)])
        visited.add((x, y))

        while queue:
            x, y = queue.popleft()
            for delta_x, delta_y in [(1, 0), (0, -1), (-1, 0), (0, 1)]:
                next_x = x + delta_x
                next_y = y + delta_y
                if not self.isValid(grid, next_x, next_y, visited):
                    continue
                queue.append((next_x, next_y))
                visited.add((next_x, next_y))
    
    def isValid(self, grid, x, y, visited):
        n, m = len(grid), len(grid[0])
        
        if not (0 <= x < n and 0 <= y < m):
            return False
        
        if (x, y) in visited:
            return False
        
        return grid[x][y] == '1'






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