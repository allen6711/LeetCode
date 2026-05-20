class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        
        rows, cols = len(board), len(board[0])
        def bfs(r: int, c: int) -> None:
            board[r][c] = "S"
            q = deque([(r, c)])
            while q:
                x, y = q.popleft()
                for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < rows and 0 <= ny < cols and board[nx][ny] == "O":
                        q.append((nx, ny))
                        board[nx][ny] = "S"
        
        for r in range(rows):
            if board[r][0] == "O":
                bfs(r, 0)
            if board[r][cols - 1] == "O":
                bfs(r, cols - 1)
        for c in range(cols):
            if board[0][c] == "O":
                bfs(0, c)
            if board[rows - 1][c] == "O":
                bfs(rows - 1, c)
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                if board[r][c] == "S":
                    board[r][c] = "O"










        # O(m * n)
        # O(m * n)
        if not board or not board[0]:
            return
        rows, cols = len(board), len(board[0])

        def bfs(r: int, c: int) -> None:
            q = deque([(r, c)])
            board[r][c] = "S"   # Mark safe

            while q:
                x, y = q.popleft()
                for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < rows and 0 <= ny < cols and board[nx][ny] == "O":
                        board[nx][ny] = "S"
                        q.append((nx, ny))
        
        for r in range(rows):
            if board[r][0] == "O":
                bfs(r, 0)
            if board[r][cols - 1] == "O":
                bfs(r, cols - 1)
        
        for c in range(cols):
            if board[0][c] == "O":
                bfs(0, c)
            if board[rows - 1][c] == "O":
                bfs(rows - 1, c)
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                if board[r][c] == "S":
                    board[r][c] = "O"
        