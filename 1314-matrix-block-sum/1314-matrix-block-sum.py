class Solution:
    def matrixBlockSum(self, mat: list[list[int]], k: int) -> list[list[int]]:
        m, n = len(mat), len(mat[0])
        numMatrix = NumMatrix(mat)
        ans = [[0] * n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                x1 = max(i - k, 0)
                y1 = max(j - k, 0)
                x2 = min(i + k, m - 1)
                y2 = min(j + k, n - 1)

                ans[i][j] = numMatrix.sumRegion(x1, y1, x2, y2)
        
        return ans

class NumMatrix:
    def __init__(self, matrix: list[list[int]]):
        m, n = len(matrix), len(matrix[0])
        self.preSum = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                self.preSum[i][j] = (self.preSum[i - 1][j] + self.preSum[i][j - 1] +
                                    matrix[i - 1][j - 1] - self.preSum[i - 1][j - 1])

    def sumRegion(self, x1, y1, x2, y2):
        return (self.preSum[x2 + 1][y2 + 1] - self.preSum[x1][y2 + 1] -
                self.preSum[x2 + 1][y1] + self.preSum[x1][y1])