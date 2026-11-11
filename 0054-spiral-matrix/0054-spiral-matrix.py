class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # Four Boundaries
        # O(m*n)
        # O(1)
        m, n = len(matrix), len(matrix[0])
        result = []
        top, bottom = 0, m - 1
        left, right = 0, n - 1

        while top <= bottom and left <= right:
            # 1. Left -> Right
            for col in range(left, right + 1):
                result.append(matrix[top][col])
            top += 1

            # 2. Top -> Bottom
            for row in range(top, bottom + 1):
                result.append(matrix[row][right])
            right -= 1

            # 3. Right -> Left
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    result.append(matrix[bottom][col])
                bottom -= 1
            
            # 4. Bottom -> Top
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    result.append(matrix[row][left])
                left += 1
        
        return result