class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        target = n * n
        def get_pos(square: int) -> tuple[int, int]:
            idx = square - 1
            row_from_bottom = idx // n
            row = n - row_from_bottom - 1
            col = idx % n
            if row_from_bottom % 2 == 1:
                col = n - col - 1
            
            return row, col
        
        q = deque([(1, 0)])
        visited = set([1])
        while q:
            cur, moves = q.popleft()
            if cur == target:
                return moves
            
            for dice in range(1, 7):
                next_square = cur + dice

                if next_square > target:
                    break
                
                r, c = get_pos(next_square)

                if board[r][c] != -1:
                    next_square = board[r][c]
                
                if next_square in visited:
                    continue
                    
                visited.add(next_square)
                q.append((next_square, moves + 1))
        
        return -1
















        # O(n^2)
        # O(n^2)
        n = len(board)
        target = n * n

        def get_pos(square: int) -> tuple[int, int]:
            idx = square - 1
            row_from_bottom = idx // n
            col = idx % n
            row = n - row_from_bottom - 1

            if row_from_bottom % 2 == 1:
                col = n - col - 1
            
            return row, col
        
        q = deque([(1, 0)])
        visited = set([1])

        while q:
            cur, moves = q.popleft()

            if cur == target:
                return moves
            
            for dice in range(1, 7):
                next_square = cur + dice
                
                if next_square > target:
                    break
                
                r, c = get_pos(next_square)

                if board[r][c] != -1:
                    next_square = board[r][c]
                
                if next_square in visited:
                    continue
                
                visited.add(next_square)
                q.append((next_square, moves + 1))
        
        return -1