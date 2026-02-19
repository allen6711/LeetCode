class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        # O(n^2)
        # O(n^2)
        m, n = len(grid), len(grid[0])
        length = m * n
        freq = [0] * (length + 1)
        for row in grid:
            for num in row:
                freq[num] += 1

        repeated = -1
        missing = -1
        
        for num in range(1, length + 1):
            if freq[num] == 2:
                repeated = num
            elif freq[num] == 0:
                missing = num
        
        return [repeated, missing]
        # O(n^2)
        # O(1)
        
