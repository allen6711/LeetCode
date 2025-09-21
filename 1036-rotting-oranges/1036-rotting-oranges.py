class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return -1
        
        m, n = len(grid), len(grid[0])
        minutes = 0
        fresh = 0
        queue = deque()
        direction = ((0, 1), (1, 0), (0, -1), (-1, 0))

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j))
                
                if grid[i][j] == 1:
                    fresh += 1
        
        if fresh == 0:
            return 0
        
        while queue:
            minutes += 1

            for _ in range(len(queue)):
                x, y = queue.popleft()

                for dx, dy in direction:
                    nx, ny = x + dx, y + dy
                    
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        fresh -= 1
                        queue.append((nx, ny))
        
        return minutes - 1 if fresh == 0 else -1




























        # if not grid or not grid[0]:
        #     return -1
        
        # m, n = len(grid), len(grid[0])
        # minutes = 0
        # fresh = 0
        # queue = deque()

        # for i in range(m):
        #     for j in range(n):
        #         if grid[i][j] == 2:
        #             queue.append((i, j))
                
        #         if grid[i][j] == 1:
        #             fresh += 1
        
        # if fresh == 0:
        #     return 0
        
        # direct = ((0, 1), (1, 0), (0, -1), (-1, 0))
        
        # while queue:
        #     minutes += 1

        #     for _ in range(len(queue)):
        #         x, y = queue.popleft()

        #         for dx, dy in direct:
        #             nx, ny = x + dx, y + dy

        #             if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
        #                 grid[nx][ny] = 2
        #                 fresh -= 1
        #                 queue.append((nx, ny))
        
        # return minutes - 1 if fresh == 0 else -1




        # if not grid or not grid[0]:
        #     return -1

        # m, n = len(grid), len(grid[0])
        # minutes = 0
        # fresh = 0
        # queue = deque()

        # for i in range(m):
        #     for j in range(n):
        #         if grid[i][j] == 2:
        #             queue.append((i, j))
                
        #         if grid[i][j] == 1:
        #             fresh += 1
        
        # if fresh == 0:
        #     return 0
        
        # dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        # while queue:
        #     minutes += 1

        #     for _ in range(len(queue)):
        #         x, y = queue.popleft()

        #         for dx, dy in dirs:
        #             nx, ny = x + dx, y + dy

        #             if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
        #                 grid[nx][ny] = 2
        #                 fresh -= 1
        #                 queue.append((nx, ny))

        # return minutes - 1 if fresh == 0 else -1


















































        # rows, cols = len(grid), len(grid[0])
        # queue = deque()
        # minutes_passed = 0
        # fresh_count = 0
        # for row in range(rows):
        #     for col in range(cols):
        #         if grid[row][col] == 2:
        #             queue.append((row, col))
        #         elif grid[row][col] == 1:
        #             fresh_count += 1
        
        # while queue and fresh_count > 0:
        #     minutes_passed += 1
        #     for _ in range(len(queue)):
        #         x, y = queue.popleft()
                
        #         for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        #             new_row, new_col = x + dx, y + dy
        #             if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] == 1:
        #                 grid[new_row][new_col] = 2
        #                 fresh_count -= 1
        #                 queue.append((new_row, new_col))
            
        # return minutes_passed if fresh_count == 0 else -1