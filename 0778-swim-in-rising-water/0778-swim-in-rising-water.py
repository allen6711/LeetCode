class Solution:
    def swimInWater(self, grid: list[list[int]]) -> int:
        n = len(grid)
        def canReach(t):
            if grid[0][0] > t:
                return False
            
            queue = deque([(0, 0)])
            visited = {(0, 0)}
            
            while queue:
                r, c = queue.popleft()
                if r == n - 1 and c == n - 1:
                    return True

                for dr, dc in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                    nr, nc = r + dr, c +dc

                    if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] <= t and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        queue.append((nr, nc))
            return False
        
        left, right = 0, n * n - 1
        while left < right:
            mid = (left + right) // 2
            if canReach(mid):
                right = mid
            else:
                left = mid + 1
        
        return left